import os
from openai import AzureOpenAI

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
                        "endpoint": "https://choiasearch.search.windows.net",  # search service쪽 개요에 있는 URL
                        "index_name": "choiindex",  # 아까 본인이 쓴
                        "authentication": {
                            "type": "api_key",
                            "key": "RhKwTUuvwD3tzaCaqHEldvWirxZWeEeI7IunFcHLbbAzSeDe7rtD",  # search service쪽 설정 - 키 - 기본 관리자 키
                        },
                        "embedding_dependency": {
                            "type": "endpoint",
                            "endpoint": "https://student02-11-2138-resource.cognitiveservices.azure.com/openai/deployments/gpt-4.1-mini/chat/completions?api-version=2025-01-01-preview",  # 내 자산 - 모델+엔드포인트 - 엔드포인트
                            "authentication": {
                                "type": "api_key",
                                "key": "8H9hpm79eW27SRapvN6vT5vbnUH8esvYS8rToIFX7WMo6psETm9BJQQJ99CBACHYHv6XJ3w3AAAAACOGBh1S",  # 내 자산 - 모델+엔드포인트 - 키
                            },
                        },
                    },
                }
            ]
        },
    )
    print(response.choices[0].message.content)
    msg.append({"role": "assistant", "content": response.choices[0].message.content})
