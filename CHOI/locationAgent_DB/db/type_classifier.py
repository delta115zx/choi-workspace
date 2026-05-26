"""
상호명 기반 업종 타입 분류기
분식/양식 가게를 세부 타입으로 분류하고 행정동 단위로 집계
"""
import csv
import re
import sys
from collections import defaultdict

# ── 분식 타입 분류 규칙 ──────────────────────────────────────────
BUNJIK_TYPE_RULES = [
    ("김밥",           ["김밥", "꼬마김밥", "충무김밥", "삼각김밥"]),
    ("떡볶이",         ["떡볶이", "즉석떡볶이", "떡볶", "라볶이", "로제떡"]),
    ("국수/칼국수",    ["국수", "칼국수", "막국수", "소면", "면가", "잔치국수"]),
    ("냉면/막국수",    ["냉면", "막국수", "물냉면", "비빔냉면"]),
    ("라면/우동",      ["라면", "우동"]),
    ("만두",           ["만두", "교자", "찐빵", "군만두", "물만두"]),
    ("순대/국밥",      ["순대", "순댓국", "국밥", "설렁탕", "해장국", "곰탕", "뼈해장", "감자탕", "추어탕"]),
    ("돈까스/카츠",    ["돈까스", "돈카츠", "왕돈까스", "카츠", "등심돈까스"]),
    ("곱창/막창",      ["곱창", "막창", "대창", "소곱창", "곱도리"]),
    ("분식포장마차",   ["어묵", "오뎅", "꽈배기", "호떡", "핫도그", "빈대떡", "부침", "전병"]),
    ("토스트/샌드위치",["토스트", "샌드위치", "샌드메이드"]),
    ("고로케/튀김",    ["고로케", "튀김", "크로켓"]),
    ("도시락",         ["도시락", "반찬", "찬"]),
    ("죽",             ["죽", "미음", "오트밀죽"]),
    ("분식(혼합)",     []),  # 위 분류 미해당 시 기본값
]

# ── 양식 타입 분류 규칙 ──────────────────────────────────────────
YANGSIK_TYPE_RULES = [
    ("파스타/이탈리안", ["파스타", "이탈리안", "리조또", "피자", "트라토리아", "오스테리아"]),
    ("스테이크/그릴",  ["스테이크", "그릴", "비프", "버거", "BBQ", "바베큐"]),
    ("브런치/카페식",  ["브런치", "카페", "비스트로", "브렉퍼스트"]),
    ("멕시칸/퓨전",   ["멕시칸", "타코", "부리또", "퓨전"]),
    ("인도/동남아",   ["인도", "카레", "커리", "타이", "태국", "베트남", "쌀국수", "포(Pho)", "인도네시아"]),
    ("프랑스/유럽",   ["프렌치", "프랑스", "갈레트", "크레페", "비엔나", "오스트리아"]),
    ("샌드위치/수제버거", ["샌드위치", "버거", "수제버거", "햄버거"]),
    ("할랄/중동",     ["할랄", "케밥", "중동", "이슬람"]),
    ("양식(기타)",    []),  # 위 분류 미해당 시 기본값
]


def classify_type(name: str, rules: list) -> str:
    name_lower = name.lower()
    for type_name, keywords in rules:
        if not keywords:
            continue
        for kw in keywords:
            if kw.lower() in name_lower:
                return type_name
    return rules[-1][0]  # 기본값 (마지막 항목)


def extract_dong(address: str) -> str:
    """도로명주소 괄호 안 동명 추출 (예: '(서교동, 건물명)' → '서교동')"""
    match = re.search(r'\(([가-힣]+동)', address)
    if match:
        return match.group(1)
    # 괄호 없으면 지번주소 패턴으로 시도
    match = re.search(r'마포구\s+([가-힣]+동)', address)
    if match:
        return match.group(1)
    return "미상"


# 분식 카테고리에 잘못 들어온 업종 필터 (상호명 기준)
BUNJIK_EXCLUDE_KEYWORDS = [
    "치킨", "통닭", "닭강정", "BBQ", "BHC", "교촌", "60계", "굽네",
    "카페", "커피", "coffee", "cafe",
    "호프", "주점", "포차", "술집", "맥주", "와인",
    "스시", "초밥", "스크린골프", "사우나", "GS25",
]


def is_excluded(name: str) -> bool:
    name_lower = name.lower()
    return any(kw.lower() in name_lower for kw in BUNJIK_EXCLUDE_KEYWORDS)


def load_mapo_stores(csv_path: str) -> tuple[list, list]:
    """마포구 분식/양식 영업중 가게 로드"""
    bunjik_stores = []
    yangsik_stores = []

    with open(csv_path, encoding='cp949') as f:
        reader = csv.DictReader(f)
        for row in reader:
            addr = row['도로명주소'].strip()
            biz = row['업태구분명'].strip()
            status = row['영업상태명'].strip()
            name = row['사업장명'].strip()
            license_date = row['인허가일자'].strip()

            if '마포구' not in addr or status != '영업/정상':
                continue

            dong = extract_dong(addr)
            store = {
                'name': name,
                'biz': biz,
                'license_date': license_date,
                'address': addr,
                'dong': dong,
            }

            if biz == '분식':
                if is_excluded(name):
                    continue
                store['type'] = classify_type(name, BUNJIK_TYPE_RULES)
                bunjik_stores.append(store)
            elif biz in {'경양식', '패밀리레스트랑', '외국음식전문점(인도,태국등)'}:
                store['type'] = classify_type(name, YANGSIK_TYPE_RULES)
                yangsik_stores.append(store)

    return bunjik_stores, yangsik_stores


def aggregate_by_dong(stores: list) -> dict:
    """행정동 × 타입 단위로 집계"""
    result = defaultdict(lambda: defaultdict(int))
    for s in stores:
        result[s['dong']][s['type']] += 1
    return result


def find_missing_types(dong_agg: dict, all_types: list) -> dict:
    """각 행정동에서 없는 타입 찾기"""
    missing = {}
    for dong, type_counts in dong_agg.items():
        absent = [t for t in all_types if type_counts.get(t, 0) == 0]
        if absent:
            missing[dong] = absent
    return missing


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    CSV_PATH = 'c:/Choi/workspace/식품_일반음식점_서울특별시.csv'

    print("데이터 로딩 중...")
    bunjik, yangsik = load_mapo_stores(CSV_PATH)
    print(f"분식 {len(bunjik)}개, 양식계열 {len(yangsik)}개 로드 완료\n")

    # ── 분식 집계 ──
    bunjik_types = [r[0] for r in BUNJIK_TYPE_RULES]
    bunjik_agg = aggregate_by_dong(bunjik)

    print("=" * 60)
    print("【마포구 분식 — 행정동별 타입 분포】")
    print("=" * 60)
    for dong in sorted(bunjik_agg):
        total = sum(bunjik_agg[dong].values())
        breakdown = ", ".join(
            f"{t}:{c}" for t, c in sorted(bunjik_agg[dong].items(), key=lambda x: -x[1])
        )
        print(f"  {dong} (총{total}) : {breakdown}")

    bunjik_missing = find_missing_types(bunjik_agg, bunjik_types[:-1])  # 혼합 제외
    print("\n【분식 — 동별 없는 타입】")
    for dong, types in sorted(bunjik_missing.items()):
        print(f"  {dong}: {', '.join(types)}")

    # ── 양식 집계 ──
    yangsik_types = [r[0] for r in YANGSIK_TYPE_RULES]
    yangsik_agg = aggregate_by_dong(yangsik)

    print("\n" + "=" * 60)
    print("【마포구 양식 — 행정동별 타입 분포】")
    print("=" * 60)
    for dong in sorted(yangsik_agg):
        total = sum(yangsik_agg[dong].values())
        breakdown = ", ".join(
            f"{t}:{c}" for t, c in sorted(yangsik_agg[dong].items(), key=lambda x: -x[1])
        )
        print(f"  {dong} (총{total}) : {breakdown}")

    yangsik_missing = find_missing_types(yangsik_agg, yangsik_types[:-1])
    print("\n【양식 — 동별 없는 타입】")
    for dong, types in sorted(yangsik_missing.items()):
        print(f"  {dong}: {', '.join(types)}")
