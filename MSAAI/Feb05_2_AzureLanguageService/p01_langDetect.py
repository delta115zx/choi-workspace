# pip install azure-ai-textanalytics==5.2.0
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "6dnAclK3gqbzuqiNkpq6qchKbAGwFURS14YtJMcSUJkZ3ZSir4YZJQQJ99CBACHYHv6XJ3w3AAAaACOGReC3"
endpoint = "https://choils.cognitiveservices.azure.com/"

tac = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

txts = ["최", "jin", "英"]
for l in tac.detect_language(txts):
    print(l.primary_language.name)