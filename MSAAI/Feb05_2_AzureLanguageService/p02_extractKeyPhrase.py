from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "6dnAclK3gqbzuqiNkpq6qchKbAGwFURS14YtJMcSUJkZ3ZSir4YZJQQJ99CBACHYHv6XJ3w3AAAaACOGReC3"
endpoint = "https://choils.cognitiveservices.azure.com/"

tac = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

txts = [
    "플레이-인에서는 그룹 대항전 기간 화제가 됐던 코치 보이스가 적용되지 않는다. 코치 보이스는 2026 LCK컵에서 그룹 대항전 기간 동안 시범 도입된 요소로, 코치진이 경기 중 정해진 횟수와 시간 안에서 선수들과 실시간 소통할 수 있도록 설계됐다."
]
results = tac.extract_key_phrases(txts)
for r in results:
    for p in r.key_phrases:
        print(p)
