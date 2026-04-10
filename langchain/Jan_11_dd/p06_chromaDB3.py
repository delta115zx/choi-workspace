from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. 모델 및 임베딩 설정 (SetupModels)
# 임베딩 모델은 처음에 추천드린 가벼운 Nomic 모델을 사용합니다.
MyEmbeddings = OllamaEmbeddings(model="Nomic-Embed-Text")
# 채팅 모델은 llama3.2:1b, 정확도를 위해 Temperature를 0으로 설정
MyLlm = ChatOllama(model="llama3.2:1b", temperature=0)

# 2. 가상데이터 설정 (CreateSampleData)
# 테스트를 위한 간단한 지식 데이터를 만듭니다.
SampleDocs = [
    Document(
        page_content="Ollama는 로컬에서 대규모 언어 모델을 실행할 수 있게 해주는 도구입니다.",
        Metadata={"Source": "OllamaGuide"},
    ),
    Document(
        page_content="ChromaDB는 벡터 검색을 지원하는 오픈소스 데이터베이스입니다.",
        Metadata={"Source": "DbInfo"},
    ),
    Document(
        page_content="Llama3.2:1b 모델은 매우 가벼우면서도 효율적인 성능을 내는 소형 언어 모델입니다.",
        Metadata={"Source": "ModelSpec"},
    ),
]

# 3. 벡터스토어 및 리트리버 구축 (BuildVectorStore)
# 데이터를 메모리에 임시 저장하거나 로컬 디렉토리에 저장하도록 설정합니다.
VectorStore = Chroma.from_documents(
    documents=SampleDocs, embedding=MyEmbeddings, persist_directory="./MyChromaDB"
)
MyRetriever = VectorStore.as_retriever(kwargs={"k": 2})

# 4. 프롬프트템플릿 정의 (DefinePrompt)
Template = """
당신은 질문에 답하는 인공지능 비서입니다. 
아래의 참고 정보를 활용하여 질문에 대해 간결하고 정확하게 답하세요.

[참고 정보]:
{Context}

[질문]:
{Question}

답변:
"""
MyPrompt = ChatPromptTemplate.from_template(Template)

# 5. LCEL체인구성 (ConstructLcelChain)
# 입력된 질문 -> 리트리버 검색 -> 프롬프트 결합 -> 모델 실행 -> 텍스트 변환
RagChain = (
    {"Context": MyRetriever, "Question": RunnablePassthrough()}
    | MyPrompt
    | MyLlm
    | StrOutputParser()
)

# 6. 시스템실행 (RunSystem)
MyQuestion = input("질문: ")
FinalResponse = RagChain.invoke(MyQuestion)

print("답변: %s" %FinalResponse)