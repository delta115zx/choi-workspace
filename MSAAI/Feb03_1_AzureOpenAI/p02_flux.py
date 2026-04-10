# 필수 패키지 설치: 'pip install requests azure-identity'
import requests
import base64
from PIL import Image
from io import BytesIO

# 이러한 환경 변수를 설정하거나 다음 값을 편집해야 합니다.
endpoint = "https://stude-ml5zsw3w-swedencentral.services.ai.azure.com/openai/deployments/FLUX-1.1-pro/images/generations?api-version=2025-04-01-preview"
deployment = "FLUX-1.1-pro"
api_version = "2025-04-01-preview"
subscription_key = "24jvqbn0DHKAaJsXH1vVlcJZzgzLUuIkSjA56aTnG8wM0kBTMO8tJQQJ99CBACfhMk5XJ3w3AAAAACOGjXtR"

def decode_and_save_image(b64_data, output_filename):
  image = Image.open(BytesIO(base64.b64decode(b64_data)))
  image.show()
  image.save(output_filename)

def save_response(response_data, filename_prefix):
  data = response_data['data']
  b64_img = data[0]['b64_json']
  filename = f"{filename_prefix}.png"
  decode_and_save_image(b64_img, filename)
  print(f"이미지 저장 장소: '{filename}'")

base_path = f'openai/deployments/{deployment}/images'
params = f'?api-version={api_version}'
myMsg = input("뭐 : ")
generation_url = f"https://stude-ml5zsw3w-swedencentral.cognitiveservices.azure.com/{base_path}/generations{params}"
generation_body = {
  "prompt": myMsg,
  "n": 1,
  "size": "1024x1024",
  "output_format": "png"
}
generation_response = requests.post(
  generation_url,
  headers={
    'Api-Key': subscription_key,
    'Content-Type': 'application/json',
  },
  json=generation_body
).json()
save_response(generation_response, "generated_image")

f = open("C:/Choi/%s.png" % myMsg, "wb")
f.write(requests.get(generation_url).content)
f.close()
