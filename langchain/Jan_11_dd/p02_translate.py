from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

# 프롬프트 템플릿 정의
prompt = ChatPromptTemplate.from_messages(
    [("system", "너는 한국어를 영어로 바꿔주는거야."), ("user", "{sentence}")]
)

# LLM 모델 정의 (Ollama 기반)
llm = ChatOllama(model="translategemma")

# 체인 구성
chain = prompt | llm

# 실행
result = chain.invoke({"sentence": "나는 게임을 좋아합니다."})
print(result.content)
