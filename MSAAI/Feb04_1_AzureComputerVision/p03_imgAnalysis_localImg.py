import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

key = os.environ["AZURE_CV_KEY"]
endpoint = os.environ["AZURE_CV_ENDPOINT"]
iac = ImageAnalysisClient(endpoint, AzureKeyCredential(key))

f = open("C:/Choi/자원2023/image/back4.jpg", "rb")
imgData = f.read()

result = iac.analyze(
    image_data=imgData,
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.OBJECTS, VisualFeatures.PEOPLE, VisualFeatures.READ]
)

# 이미지 주제 찾기 
print("caption")
if result.caption is not None:
    print(result.caption.text, result.caption.confidence)
print("-----")

# 객체
print("object")
if result.objects is not None:
    print(result.objects)

# 사람
print("caption")
if result.people is not None:
    print(result.people)
print("-----")

# OCR
print("read")
if result.read is not None:
    print(result.read)
print("-----")
