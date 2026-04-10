from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

# 1. 임베딩 모델 설정
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# 2. 간단한 데이터 예시
docs = [
    Document(page_content="Ollama는 로컬에서 LLM을 실행하게 해주는 도구입니다."),
    Document(page_content="ChromaDB는 오픈소스 벡터 데이터베이스입니다."),
    Document(page_content="LangChain은 AI 애플리케이션 프레임워크입니다."),
]

# 3. ChromaDB 생성 및 저장
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chromaDB",  # 데이터를 로컬에 저장
)

# 4. 벡터 검색 수행
query = input("검색 : ")
results = vectorstore.similarity_search(query, k=1)

print("검색 결과: %s" % results[0].page_content)
