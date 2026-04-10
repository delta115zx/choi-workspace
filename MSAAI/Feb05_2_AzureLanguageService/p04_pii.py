# PII(Personal Identifying Information)
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "6dnAclK3gqbzuqiNkpq6qchKbAGwFURS14YtJMcSUJkZ3ZSir4YZJQQJ99CBACHYHv6XJ3w3AAAaACOGReC3"
endpoint = "https://choils.cognitiveservices.azure.com/"

tac = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

txts = [
    "권기웅, 수석강사/학과장, 02-6901-7000, bean_mouse@soldesk.com, 서울특별시 종로구 종로12"
]

results = tac.recognize_pii_entities(documents=txts)
for r in results:
    print("기밀 ", r.redacted_text)
    for e in r.entities:
        print(e)