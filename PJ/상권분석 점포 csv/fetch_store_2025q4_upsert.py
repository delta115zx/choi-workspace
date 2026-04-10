"""
fetch_store_2025q4_upsert.py
2025년 4분기 점포 데이터 수집 → CSV 저장 → Azure PostgreSQL 적재
  - 테이블: sangkwon_store (integrated_PARK/db/schema_pg.sql 기준)
  - 적재 방식: 해당 분기 기존 행 삭제 후 INSERT (re-run 안전)
"""

import requests
import csv
import os
import time
import psycopg2
import psycopg2.extras

# ── API 설정 ────────────────────────────────────────────────
API_KEY   = "52414b6f6164656c363261586a4e4f"
SERVICE   = "VwsmAdstrdStorW"
BASE_URL  = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/{SERVICE}"
QUARTER   = "20254"   # 2025년 4분기
PAGE_SIZE = 1000

OUTPUT_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "store_adstrd_2025q4.csv")

# ── PostgreSQL 설정 ─────────────────────────────────────────
DB_CONFIG = {
    "host":     "sohobi-db-prod.postgres.database.azure.com",
    "port":     5432,
    "dbname":   "sohobi",
    "user":     "sohobi_admin",
    "password": "MSSAY2-2",
    "sslmode":  "require",
}

TABLE_NAME = "sangkwon_store"

# API 응답 컬럼
API_COLUMNS = [
    "STDR_YYQU_CD",
    "ADSTRD_CD",
    "ADSTRD_CD_NM",
    "SVC_INDUTY_CD",
    "SVC_INDUTY_CD_NM",
    "STOR_CO",
    "SIMILR_INDUTY_STOR_CO",
    "OPBIZ_RT",
    "OPBIZ_STOR_CO",
    "CLSBIZ_RT",
    "CLSBIZ_STOR_CO",
    "FRC_STOR_CO",
]

# CSV 헤더 (DB 컬럼명 기준)
CSV_COLUMNS = [
    "base_yr_qtr_cd",
    "adm_cd",
    "adm_nm",
    "svc_induty_cd",
    "svc_induty_nm",
    "stor_co",
    "similr_induty_stor_co",
    "opbiz_rt",
    "opbiz_stor_co",
    "clsbiz_rt",
    "clsbiz_stor_co",
    "frc_stor_co",
]

# DB INSERT 컬럼 (id는 BIGSERIAL 자동 생성)
DB_COLUMNS = CSV_COLUMNS


def api_row_to_db(row: dict) -> tuple:
    """API 응답 행 → DB INSERT용 tuple (API컬럼명 → DB컬럼명 매핑)"""
    def num(val):
        if val == "" or val is None:
            return None
        try:
            return float(val)
        except (ValueError, TypeError):
            return None

    return (
        row.get("STDR_YYQU_CD") or None,
        row.get("ADSTRD_CD") or None,
        row.get("ADSTRD_CD_NM") or None,
        row.get("SVC_INDUTY_CD") or None,
        row.get("SVC_INDUTY_CD_NM") or None,
        num(row.get("STOR_CO")),
        num(row.get("SIMILR_INDUTY_STOR_CO")),
        num(row.get("OPBIZ_RT")),
        num(row.get("OPBIZ_STOR_CO")),
        num(row.get("CLSBIZ_RT")),
        num(row.get("CLSBIZ_STOR_CO")),
        num(row.get("FRC_STOR_CO")),
    )


# ── API 함수 ────────────────────────────────────────────────
def fetch_total_count(quarter: str) -> int:
    url = f"{BASE_URL}/1/1/{quarter}"
    res = requests.get(url, timeout=30)
    data = res.json()
    return data[SERVICE]["list_total_count"]


def fetch_page(start: int, end: int, quarter: str) -> list:
    url = f"{BASE_URL}/{start}/{end}/{quarter}"
    res = requests.get(url, timeout=30)
    data = res.json()
    result = data.get(SERVICE, {})
    code = result.get("RESULT", {}).get("CODE", "")
    if code != "INFO-000":
        print(f"  API 오류: {result.get('RESULT', {}).get('MESSAGE', '')}")
        return []
    return result.get("row", [])


# ── DB 함수 ─────────────────────────────────────────────────
def delete_quarter(conn, quarter: str) -> int:
    with conn.cursor() as cur:
        cur.execute(
            f"DELETE FROM {TABLE_NAME} WHERE base_yr_qtr_cd = %s",
            (quarter,)
        )
        deleted = cur.rowcount
    conn.commit()
    return deleted


def insert_rows(conn, rows: list) -> int:
    if not rows:
        return 0

    col_str = ", ".join(DB_COLUMNS)
    placeholders = ", ".join(["%s"] * len(DB_COLUMNS))
    sql = f"INSERT INTO {TABLE_NAME} ({col_str}) VALUES ({placeholders})"

    data = [api_row_to_db(row) for row in rows]

    with conn.cursor() as cur:
        psycopg2.extras.execute_batch(cur, sql, data, page_size=500)
    conn.commit()
    return len(data)


# ── 메인 ────────────────────────────────────────────────────
def main():
    print(f"=== 2025년 4분기 ({QUARTER}) 점포 데이터 수집 ===\n")

    # 1) 총 건수 확인
    total = fetch_total_count(QUARTER)
    total_pages = (total + PAGE_SIZE - 1) // PAGE_SIZE
    print(f"총 {total:,}건 / {total_pages}페이지\n")

    # 2) API 수집 + CSV 저장
    all_rows = []
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()

        for page in range(total_pages):
            start = page * PAGE_SIZE + 1
            end   = min(start + PAGE_SIZE - 1, total)
            print(f"  페이지 {page+1}/{total_pages} ({start}~{end}) 수집 중...", end=" ", flush=True)

            rows = fetch_page(start, end, QUARTER)
            if rows:
                for row in rows:
                    writer.writerow({
                        db_col: row.get(api_col, "")
                        for db_col, api_col in zip(CSV_COLUMNS, API_COLUMNS)
                    })
                all_rows.extend(rows)
                print(f"{len(rows)}건")
            else:
                print("0건 (오류)")

            time.sleep(0.3)

    print(f"\nCSV 저장 완료: {OUTPUT_CSV} ({len(all_rows):,}건)\n")

    # 3) PostgreSQL 적재
    print("=== PostgreSQL 적재 시작 ===")
    print(f"  호스트: {DB_CONFIG['host']}")
    print(f"  DB:     {DB_CONFIG['dbname']}")
    print(f"  테이블: {TABLE_NAME}\n")

    conn = psycopg2.connect(**DB_CONFIG)
    try:
        # 기존 동일 분기 데이터 삭제 (re-run 안전)
        deleted = delete_quarter(conn, QUARTER)
        if deleted:
            print(f"기존 {QUARTER} 데이터 {deleted:,}건 삭제")

        inserted = insert_rows(conn, all_rows)
        print(f"INSERT 완료: {inserted:,}건 → {TABLE_NAME}")
    finally:
        conn.close()

    print("\n전체 작업 완료!")


if __name__ == "__main__":
    main()
