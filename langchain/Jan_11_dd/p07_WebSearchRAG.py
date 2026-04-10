from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. 모델 설정 (SetupModels)
# 채팅 모델은 llama3.2:1b, 정확도를 위해 Temperature를 0으로 설정
MyLlm = ChatOllama(model="llama3.2:1b", temperature=0)

# 2. 검색도구설정 (SetupSearchTool)
# DuckDuckGo 검색 도구를 생성합니다.
SearchTool = DuckDuckGoSearchRun()


# 3. 검색실행함수 (DefineSearchFunction)
# 질문을 받아 웹에서 검색한 텍스트를 반환하는 간단한 함수입니다.
def WebSearchFunction(InputData):
    Question = InputData["Question"]
    return SearchTool.run(Question)


# 4. 프롬프트템플릿작성 (CreateWebPrompt)
Template = """
당신은 실시간 웹 검색 결과를 바탕으로 답변하는 유능한 비서입니다.
아래의 [Web_Context] 내용을 참고하여 [Question]에 친절하게 답하세요.

[Web_Context]: 
{Context}

[Question]: 
{Question}

답변:
"""
MyPrompt = ChatPromptTemplate.from_template(Template)

# 5. LCEL체인구성 (ConstructLcelChain)
# 입력된 질문 -> 리트리버 검색 -> 프롬프트 결합 -> 모델 실행 -> 텍스트 변환
WebRagChain = (
    {"Context": WebSearchFunction, "Question": RunnablePassthrough()}
    | MyPrompt
    | MyLlm
    | StrOutputParser()
)

# 6. 실행 (RunSearch)
MyQuestion = input("질문: ")
Response = WebRagChain.invoke({"Question": MyQuestion})

print("답변: %s" % Response)
