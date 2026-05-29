"""
fetch_sales_2025q4_upsert.py
2025년 4분기 매출 데이터 수집 → CSV 저장 → Azure PostgreSQL 적재
  - API: VwsmAdstrdSelngW (행정동별 업종 매출)
  - 테이블: sangkwon_sales (integrated_PARK/db/schema_pg.sql 기준)
  - 적재 방식: 해당 분기 기존 행 삭제 후 INSERT (re-run 안전)
"""

import requests
import csv
import os
import time
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# ── API 설정 ────────────────────────────────────────────────
API_KEY   = os.environ["SEOUL_API_KEY"]
SERVICE   = "VwsmAdstrdSelngW"
BASE_URL  = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/{SERVICE}"
QUARTER   = "20254"
PAGE_SIZE = 1000

OUTPUT_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sales_adstrd_2025q4.csv")

# ── PostgreSQL 설정 ─────────────────────────────────────────
DB_CONFIG = {
    "host":     os.environ["PG_HOST"],
    "port":     int(os.getenv("PG_PORT", "5432")),
    "dbname":   os.getenv("PG_DBNAME", "sohobi"),
    "user":     os.environ["PG_USER"],
    "password": os.environ["PG_PASSWORD"],
    "sslmode":  "require",
}

TABLE_NAME = "sangkwon_sales"

# API 응답 키 → DB 컬럼명 매핑 (schema_pg.sql 기준)
FIELD_MAP = [
    ("STDR_YYQU_CD",            "base_yr_qtr_cd"),
    ("ADSTRD_CD",               "adm_cd"),
    ("ADSTRD_CD_NM",            "adm_nm"),
    ("SVC_INDUTY_CD",           "svc_induty_cd"),
    ("SVC_INDUTY_CD_NM",        "svc_induty_nm"),
    ("THSMON_SELNG_AMT",        "tot_sales_amt"),
    ("THSMON_SELNG_CO",         "tot_selng_co"),
    ("MDWK_SELNG_AMT",          "mdwk_sales_amt"),
    ("WKEND_SELNG_AMT",         "wkend_sales_amt"),
    ("MON_SELNG_AMT",           "mon_sales_amt"),
    ("TUES_SELNG_AMT",          "tue_sales_amt"),
    ("WED_SELNG_AMT",           "wed_sales_amt"),
    ("THUR_SELNG_AMT",          "thu_sales_amt"),
    ("FRI_SELNG_AMT",           "fri_sales_amt"),
    ("SAT_SELNG_AMT",           "sat_sales_amt"),
    ("SUN_SELNG_AMT",           "sun_sales_amt"),
    ("TMZON_00_06_SELNG_AMT",   "tm00_06_sales_amt"),
    ("TMZON_06_11_SELNG_AMT",   "tm06_11_sales_amt"),
    ("TMZON_11_14_SELNG_AMT",   "tm11_14_sales_amt"),
    ("TMZON_14_17_SELNG_AMT",   "tm14_17_sales_amt"),
    ("TMZON_17_21_SELNG_AMT",   "tm17_21_sales_amt"),
    ("TMZON_21_24_SELNG_AMT",   "tm21_24_sales_amt"),
    ("ML_SELNG_AMT",            "ml_sales_amt"),
    ("FML_SELNG_AMT",           "fml_sales_amt"),
    ("AGRDE_10_SELNG_AMT",      "age10_amt"),
    ("AGRDE_20_SELNG_AMT",      "age20_amt"),
    ("AGRDE_30_SELNG_AMT",      "age30_amt"),
    ("AGRDE_40_SELNG_AMT",      "age40_amt"),
    ("AGRDE_50_SELNG_AMT",      "age50_amt"),
    ("AGRDE_60_ABOVE_SELNG_AMT","age60_amt"),
]

API_KEYS   = [fm[0] for fm in FIELD_MAP]
DB_COLUMNS = [fm[1] for fm in FIELD_MAP]


def to_bigint(val):
    """float 형태 문자열 또는 숫자 → 정수 (None 처리 포함)"""
    if val is None or val == "":
        return None
    try:
        return int(float(val))
    except (ValueError, TypeError):
        return None


def api_row_to_tuple(row: dict) -> tuple:
    result = []
    for api_key, db_col in FIELD_MAP:
        val = row.get(api_key)
        if db_col in ("base_yr_qtr_cd", "adm_cd", "adm_nm", "svc_induty_cd", "svc_induty_nm"):
            result.append(val or None)
        else:
            result.append(to_bigint(val))
    return tuple(result)


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

    col_str      = ", ".join(DB_COLUMNS)
    placeholders = ", ".join(["%s"] * len(DB_COLUMNS))
    sql = f"INSERT INTO {TABLE_NAME} ({col_str}) VALUES ({placeholders})"

    data = [api_row_to_tuple(row) for row in rows]

    with conn.cursor() as cur:
        psycopg2.extras.execute_batch(cur, sql, data, page_size=500)
    conn.commit()
    return len(data)


# ── 메인 ────────────────────────────────────────────────────
def main():
    print(f"=== 2025년 4분기 ({QUARTER}) 매출 데이터 수집 ===\n")

    # 1) 총 건수 확인
    total = fetch_total_count(QUARTER)
    total_pages = (total + PAGE_SIZE - 1) // PAGE_SIZE
    print(f"총 {total:,}건 / {total_pages}페이지\n")

    # 2) API 수집 + CSV 저장
    all_rows = []
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=DB_COLUMNS)
        writer.writeheader()

        for page in range(total_pages):
            start = page * PAGE_SIZE + 1
            end   = min(start + PAGE_SIZE - 1, total)
            print(f"  페이지 {page+1}/{total_pages} ({start}~{end}) 수집 중...", end=" ", flush=True)

            rows = fetch_page(start, end, QUARTER)
            if rows:
                for row in rows:
                    writer.writerow({
                        db_col: row.get(api_key, "")
                        for api_key, db_col in FIELD_MAP
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
