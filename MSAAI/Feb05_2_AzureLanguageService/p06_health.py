# NER(Named Entity Recog)
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

key = os.environ["AZURE_LANGUAGE_KEY"]
endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]

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