# NER(Named Entity Recog)
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "6dnAclK3gqbzuqiNkpq6qchKbAGwFURS14YtJMcSUJkZ3ZSir4YZJQQJ99CBACHYHv6XJ3w3AAAaACOGReC3"
endpoint = "https://choils.cognitiveservices.azure.com/"

tac = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

txts = [
    """광무제는 백성들에게 조세를 감면해 주고 형을 가벽게 하는 등의 선행을 베풀어 
민심을 끌어들임으로써  나라를 중흥시켰다.그러나  후한의 가장 큰  골칫거리는 
외척들이 득세하여 권세를  희롱하는 것이었다.그들은 후한 초기부터  고개를 들
기 시작하더니 몇대를  거치면서 권력을 맘대로 휘드르며  정사를 어지럽혔다.이
대로 간다면 황실은 그야말로 실권없는 허수아비에 불과할 것이 뻔했다.
황제는 궁리 끝에 외척을 몰아내기  위해서는 자신의 직속이라고 할 수 있는 궁
내관의 힘을 빌려야  한다고 생각했다.궁내관은 대다수가 내시라고  하는 환관들
이었다.이 환관이란 본디  궁녀들을 감독 관리하는 직무로서 거세된 자들이었다. 
그러나 권력의 중심부에 있었기  때문에 과거 춘추 전국시대부터 조정에 상당한 
영향력을 행사했으며 광무제 때부터는 정사어ㅔ도 관여하고 있었다.
황제는 자기의 결심을  항상 환관의 우두머리인 조절과 의논했다.조절을  제 9대 
황제인 순제가 황세자이던 때에 같이 공부를 한 인연으로 11대 환제에 이르기까
지 3제를 섬겨 오고 있었다.더구나 환제가  황제의 자리에 오르는 데에도 남달리 
고이 컸다.그런 조절이고 보니 황제로서도 믿을 수 있는 인물이었다.
조절도 외척의 득세를 눈엣가시처럼 여기고 있던  터였다.황제의 의중을 알게 된 
조절은 곧  선초.조관등을 비롯한 다섯  명의 환관들을 계책에  끌여들여 외척을 
몰아 내는 데 성공했다.세상은 금세 환관들의 세상으로 변하고 말았다.공적을 세
운 환관들은 열후에  봉해졌고 ,조정의 고과에서부터 지방관에  이르기까지 환관
가 연줄이 닿는 사람들로 채워졌다.
"""
]

results = tac.recognize_entities(documents=txts)
for r in results:
    for e in r.entities:
        print(e)
