# pip install azure-ai-textanalytics==5.2.0
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

key = os.environ["AZURE_LANGUAGE_KEY"]
endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]

tac = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

txts = ["최", "jin", "英"]
for l in tac.detect_language(txts):
    print(l.primary_language.name)