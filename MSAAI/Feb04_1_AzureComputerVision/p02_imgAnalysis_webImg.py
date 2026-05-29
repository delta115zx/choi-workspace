# pip install azure-ai-vision-imageanalysis
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

key = os.environ["AZURE_CV_KEY"]
endpoint = os.environ["AZURE_CV_ENDPOINT"]
iac = ImageAnalysisClient(endpoint, AzureKeyCredential(key))

imgURL = "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5002%2F2023%2F12%2F31%2F0002500994_001_20231231163601958.jpg&type=sc960_832"

result = iac.analyze_from_url(
    image_url=imgURL,
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
