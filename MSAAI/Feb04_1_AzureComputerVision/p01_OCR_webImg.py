# pip install azure-cognitiveservices-vision-computervision
# pip install pillow

import os
from time import sleep
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv

load_dotenv()

key = os.environ["AZURE_CV_KEY"]
endpoint = os.environ["AZURE_CV_ENDPOINT"]

cvc = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

imgURL = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNTA2MjZfMzgg%2FMDAxNzUwODY2MDYwODQ2.MI9iRtKmmx89_QtBwpX7g-Czk53whWoVFc4RG-FkKB0g.koJUha0YCF6cLPB6P67xwWzNha8HSJe4Hhtmo-aVOHog.JPEG%2F6U3A5776.JPG&type=sc960_832"

res = cvc.read(imgURL, raw=True)
ol = res.headers["Operation-Location"]
oID = ol.split("/")[-1]

while True:
    result = cvc.get_read_result(oID)
    if result.status not in ["notStarted", "running"]:
        break
    sleep(1)

if result.status == OperationStatusCodes.succeeded:
    for result2 in result.analyze_result.read_results:
        for line in result2.lines:
            print(line.text, line.bounding_box)
