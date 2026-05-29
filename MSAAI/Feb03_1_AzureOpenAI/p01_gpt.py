import os
from openai import AzureOpenAI
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

msg = [{"role": "system", "content": "openwheather 정보 알려주는 AI 도우미"}]

while True:
    myMsg = input("뭐 : ")
    if myMsg == "종료":
        break
    msg.append({"role": "user", "content": myMsg})
    response = client.chat.completions.create(
        model=deployment,
        messages=msg,
        extra_body={
            "data_sources": [
                {
                    "type": "azure_search",
                    "parameters": {
                        "endpoint": os.environ["AZURE_SEARCH_ENDPOINT"],
                        "index_name": os.environ["AZURE_SEARCH_INDEX"],
                        "authentication": {
                            "type": "api_key",
                            "key": os.environ["AZURE_SEARCH_KEY"],
                        },
                        "embedding_dependency": {
                            "type": "endpoint",
                            "endpoint": os.environ["AZURE_OPENAI_ENDPOINT"],
                            "authentication": {
                                "type": "api_key",
                                "key": os.environ["AZURE_OPENAI_API_KEY"],
                            },
                        },
                    },
                }
            ]
        },
    )
    print(response.choices[0].message.content)
    msg.append({"role": "assistant", "content": response.choices[0].message.content})
