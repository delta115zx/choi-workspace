# pip install azure-ai-translation-document==1.1.0b1
# 파일 -번역-> 파일 : 필요하다면 그 파일 만들기위한 추가 lib도 설치
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import SingleDocumentTranslationClient
from azure.ai.translation.document.models import DocumentTranslateContent

key = "6eoOH0cGTDtr3TDzwrJ43ZS2bOd4hQaxE0Nvk2c5UKXW4xvfj5aIJQQJ99CBACHYHv6XJ3w3AAAbACOGZfhm"
endpoint = "https://choitranslator.cognitiveservices.azure.com/"

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
