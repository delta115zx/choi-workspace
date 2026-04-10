from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# 추천드린 nomic-embed-text 모델 사용
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Chroma DB 초기화
vector_store = Chroma(
    collection_name="my_docs",
    embedding_function=embeddings,
    persist_directory="./my_chroma_db",  # 로컬에 데이터를 저장할 경로
)

documents = [
    Document(
        page_content="Ollama는 아주 가벼운 로컬 LLM 실행 도구입니다.",
        metadata={"source": "ollama_guide"},
    ),
    Document(
        page_content="ChromaDB는 오픈소스 벡터 데이터베이스입니다.",
        metadata={"source": "db_info"},
    ),
]

# DB에 추가
vector_store.add_documents(documents=documents)

# 유사도 검색
results = vector_store.similarity_search("로컬에서 쓰는 LLM 도구는?", k=1)
for res in results:
    print("찾은 내용: %s" % res.page_content)

# 점수포함
results_with_score = vector_store.similarity_search_with_score("벡터 DB란?", k=1)
for res, score in results_with_score:
    print("내용: %s (점수: %s)" % (res.page_content, score))

# 리트리버로 변환
retriever = vector_store.as_retriever(
    search_type="similarity",   # 혹은 "mmr" (다양성 강조 검색)
    search_kwargs={"k": 2}      # 2개 검색
)