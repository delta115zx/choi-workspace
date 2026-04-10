# pip install azure-ai-translation-text==1.0.0b1
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

key = "6eoOH0cGTDtr3TDzwrJ43ZS2bOd4hQaxE0Nvk2c5UKXW4xvfj5aIJQQJ99CBACHYHv6XJ3w3AAAbACOGZfhm"
endpoint = "https://api.cognitive.microsofttranslator.com/"
region = "eastus2"

tc = TranslatorCredential(key, region)
ttc = TextTranslationClient(credential=tc, endpoint=endpoint)
targetLang = ["en", "ja", "fr", "zh-Hans"]

txt = input("뭐 : ")
itis = [InputTextItem(text=txt)]

res = ttc.translate(content=itis, to=targetLang)
print(res)