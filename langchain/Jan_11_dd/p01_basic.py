from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 모델 로드
llm = ChatOllama(model="translategemma:latest", temperature=0.5)

# 프롬프트 템플릿 설정 (선택사항이지만 권장)
prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant."), ("user", "{input}")]
)

# 출력 파서 설정 (LLM의 출력을 문자열로 파싱)
outputParser = StrOutputParser()

# 체인 구성
chain = prompt | llm | outputParser

# 답변 요청
question = input("질문 : ")
response = chain.invoke({"input": question})

# 답변 출력
print(f"답변: {response}")
