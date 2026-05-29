import json
import os
from openai import AzureOpenAI
import requests
from dotenv import load_dotenv

load_dotenv()

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
model_name = "gpt-4.1-mini"
deployment = "gpt-4.1-mini"

subscription_key = os.environ["AZURE_OPENAI_API_KEY"]
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

while True:
    myMsg = input("뭐 : ")
    if myMsg == "종료":
        break

    result = client.images.generate(model="dall-e-3", prompt=myMsg, n=1)

    json_response = json.loads(result.model_dump_json())
    image_url = json_response["data"][0]["url"]
    print(image_url)

    f = open("C:/Choi/%s.png" % myMsg, "wb")
    f.write(requests.get(image_url).content)
    f.close()