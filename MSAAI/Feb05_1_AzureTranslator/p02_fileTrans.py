# pip install azure-ai-translation-document==1.1.0b1
# 파일 -번역-> 파일 : 필요하다면 그 파일 만들기위한 추가 lib도 설치
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import SingleDocumentTranslationClient
from azure.ai.translation.document.models import DocumentTranslateContent
from dotenv import load_dotenv

load_dotenv()

key = os.environ["AZURE_TRANSLATOR_KEY"]
endpoint = os.environ["AZURE_TRANSLATOR_ENDPOINT"]

sdtc = SingleDocumentTranslationClient(endpoint, AzureKeyCredential(key))

filePath = "C:/Choi/질문(개발+MS).xlsx"
fileName = filePath.split("/")[-1]
fileType = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

f = open(filePath, "rb")
fileContents = f.read()
f.close()

docContent = (fileName, fileContents, fileType)
dtc = DocumentTranslateContent(document=docContent)
result = sdtc.document_translate(body=dtc, target_language="en")

f2 = open("C:/Choi/질문(번역된거).xlsx", "wb")
f2.write(result)
f2.close()
