"""
소상공인 상가정보 API — 서울시 음식 소분류 코드 조회
divId=ctprvnCd, key=11 (서울) + 중분류 필터로 소분류 현황 파악
"""
import json
import sys
import time
import os
import urllib.request
import urllib.parse
from collections import Counter
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../.env"))

API_KEY = os.environ["SGNG_API_KEY"]
BASE_URL = "https://apis.data.go.kr/B553077/api/open/sdsc2/storeListInDong"

FOOD_MCLS = [
    ("I205", "분식"),
    ("I201", "한식"),
    ("I204", "양식"),
    ("I203", "일식"),
]


def fetch_all_pages(mcls_cd: str) -> list:
    results = []
    page = 1

    while True:
        params = urllib.parse.urlencode({
            "serviceKey": API_KEY,
            "divId": "ctprvnCd",
            "key": "11",
            "indsLclsCd": "I2",
            "indsMclsCd": mcls_cd,
            "pageNo": page,
            "numOfRows": 1000,
            "type": "json",
        })
        url = BASE_URL + "?" + params

        raw = None
        for attempt in range(5):
            try:
                with urllib.request.urlopen(url, timeout=30) as resp:
                    raw = resp.read()
                break
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    time.sleep(2 ** attempt)
                else:
                    print(f"  HTTP {e.code}")
                    return results
            except Exception as e:
                print(f"  오류: {e}")
                return results

        if raw is None:
            print("  429 재시도 초과")
            break

        time.sleep(0.3)

        data = json.loads(raw.decode("utf-8", errors="replace"))
        body = data.get("body", {})
        items = body.get("items", [])

        if not items:
            break

        results.extend(items)

        total = int(body.get("totalCount", 0))
        if len(results) >= total:
            break

        page += 1

    return results


def main():
    print("=" * 60)
    print("서울시 음식업종 소분류 코드 현황")
    print("=" * 60)

    for mcls_cd, mcls_nm in FOOD_MCLS:
        print(f"\n> {mcls_nm}({mcls_cd})")

        items = fetch_all_pages(mcls_cd)
        total = len(items)
        print(f"  총 {total:,}개 업소")

        scls_counter = Counter()
        for item in items:
            code = item.get("indsSclsCd", "없음")
            name = item.get("indsSclsNm", "없음")
            scls_counter[(code, name)] += 1

        print(f"  소분류 {len(scls_counter)}종:")
        for (code, name), cnt in sorted(scls_counter.items(), key=lambda x: -x[1]):
            pct = cnt / total * 100 if total else 0
            print(f"    {code}  {name:<22}  {cnt:5,}개  ({pct:.1f}%)")


if __name__ == "__main__":
    main()
