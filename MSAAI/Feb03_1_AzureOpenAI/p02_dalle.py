import json
from openai import AzureOpenAI
import requests

endpoint = "https://student02-11-2138-resource.cognitiveservices.azure.com/"
model_name = "gpt-4.1-mini"
deployment = "gpt-4.1-mini"

subscription_key = "8H9hpm79eW27SRapvN6vT5vbnUH8esvYS8rToIFX7WMo6psETm9BJQQJ99CBACHYHv6XJ3w3AAAAACOGBh1S"
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