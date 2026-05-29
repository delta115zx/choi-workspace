# pip install azure-ai-translation-text==1.0.0b1
import os
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from dotenv import load_dotenv

load_dotenv()

key = os.environ["AZURE_TRANSLATOR_KEY"]
endpoint = "https://api.cognitive.microsofttranslator.com/"
region = os.getenv("AZURE_TRANSLATOR_REGION", "eastus2")

tc = TranslatorCredential(key, region)
ttc = TextTranslationClient(credential=tc, endpoint=endpoint)
targetLang = ["en", "ja", "fr", "zh-Hans"]

txt = input("뭐 : ")
itis = [InputTextItem(text=txt)]

res = ttc.translate(content=itis, to=targetLang)
print(res)