# Before running the sample:
#    pip install --pre azure-ai-projects>=2.0.0b1
#    pip install azure-identity

# 컴에
# Azure CLI설치
# 이 파일 있는곳에 가서 cmd
# az login -> 로그인 하고나서
# python p03_agent.py로 실행

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

myEndpoint = "https://student02-11-2138-resource.services.ai.azure.com/api/projects/student02_11-2138"

project_client = AIProjectClient(
    endpoint=myEndpoint,
    credential=DefaultAzureCredential(),
)

myAgent = "choi-agent"
# Get an existing agent
agent = project_client.agents.get(agent_name=myAgent)
print(f"Retrieved agent: {agent.name}")

openai_client = project_client.get_openai_client()

myMsg = input("뭐 : ")
# Reference the agent to get a response
response = openai_client.responses.create(
    input=[{"role": "user", "content": myMsg}],
    extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
)

print(f"Response output: {response.output_text}")
