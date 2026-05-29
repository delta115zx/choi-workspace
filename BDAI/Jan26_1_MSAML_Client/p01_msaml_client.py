# 나중에 MS Azure AI 클라이언트 할때 필요
# pip install azure-ai-ml
# pip install azure-identity
#####
import os
import urllib.request
import json
from dotenv import load_dotenv

load_dotenv()

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
    "input_data": {"columns": ["fight", "yok"], "index": [0], "data": [[80, 20]]},
}

body = str.encode(json.dumps(data))

url = os.environ["AZURE_ML_ENDPOINT"]
api_key = os.environ["AZURE_ML_API_KEY"]
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": ("Bearer " + api_key),
}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    result = json.loads(result)[0]
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", "ignore"))
