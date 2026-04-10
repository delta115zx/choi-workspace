# NER(Named Entity Recog)
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "6dnAclK3gqbzuqiNkpq6qchKbAGwFURS14YtJMcSUJkZ3ZSir4YZJQQJ99CBACHYHv6XJ3w3AAAaACOGReC3"
endpoint = "https://choils.cognitiveservices.azure.com/"

tac = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

txts = [
    "타이레놀 2개씩 아플때마다 먹고, 후시딘 씻고나서 상처난데 조금씩 바르고, 구내염 생긴곳에 알보칠 조금씩 발라서 지지고",
    "감기에는 약이 없고"
]

results = tac.begin_analyze_healthcare_entities(documents=txts)
for r in results.result():
    for e in r.entities:
        print(e.text)
        print(e.normalized_text)
        print(e.category)
        print(e.subcategory)
        print("-----")