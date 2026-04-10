"""
fetch_store_api.py
서울시 상권분석서비스 점포 API (VwsmAdstrdStorW) → CSV 저장
- 행정동 단위 점포수 / 개폐업률 데이터
- 분기별 1000개씩 페이징 요청
- 수집 범위: 2019년 1분기 ~ 2025년 3분기
"""

import requests
import csv
import os
import time

API_KEY    = "52414b6f6164656c363261586a4e4f"
SERVICE    = "VwsmAdstrdStorW"
BASE_URL   = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/{SERVICE}"
OUTPUT_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "store_adstrd.csv")
PAGE_SIZE  = 1000

def generate_quarters(start_year, start_q, end_year, end_q) -> list:
    quarters = []
    year, q = start_year, start_q
    while (year, q) <= (end_year, end_q):
        quarters.append(f"{year}{q}")
        q += 1
        if q > 4:
            q = 1
            year += 1
    return quarters

QUARTERS = generate_quarters(2019, 1, 2025, 3)

COLUMNS = [
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


def main():
    print(f"수집 분기: {QUARTERS[0]} ~ {QUARTERS[-1]} ({len(QUARTERS)}개 분기)")
    print(f"저장 경로: {OUTPUT_CSV}\n")

    total_saved = 0

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()

        for qi, quarter in enumerate(QUARTERS):
            print(f"\n[{qi+1}/{len(QUARTERS)}] 분기: {quarter} 처리 중...")

            total = fetch_total_count(quarter)
            total_pages = (total + PAGE_SIZE - 1) // PAGE_SIZE
            print(f"  총 {total:,}건 / {total_pages}페이지")

            quarter_saved = 0
            for page in range(total_pages):
                start = page * PAGE_SIZE + 1
                end   = min(start + PAGE_SIZE - 1, total)

                rows = fetch_page(start, end, quarter)
                if rows:
                    for row in rows:
                        writer.writerow({col: row.get(col, "") for col in COLUMNS})
                    quarter_saved += len(rows)

                time.sleep(0.3)

            total_saved += quarter_saved
            print(f"  {quarter} 완료: {quarter_saved:,}건 (누적: {total_saved:,}건)")

    print(f"\n전체 완료! 총 {total_saved:,}건 저장 → {OUTPUT_CSV}")


if __name__ == "__main__":
    main()