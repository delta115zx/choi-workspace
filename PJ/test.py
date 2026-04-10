import os
from typing import List, Dict, Any
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from dotenv import load_dotenv

# .env 로드
load_dotenv()

# --- 환경 변수 설정 ---
SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX_NAME")

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv("AZURE_EMBEDDING_DEPLOYMENT")
AZURE_API_VERSION = os.getenv("AZURE_EMBEDDING_API_VERSION", "2024-02-01")

# --- 클라이언트 초기화 ---
ai_client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version=AZURE_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)

search_client = SearchClient(
    endpoint=SEARCH_ENDPOINT,
    index_name=INDEX_NAME,
    credential=AzureKeyCredential(SEARCH_KEY)
)

def perform_vector_search(query_text: str, top_k: int = 3):
    """
    텍스트 기반으로 확인된 법령 필드 구조에 맞춰 벡터 검색을 수행합니다.
    대상 필드: fullText_vector
    """
    if not query_text:
        return []

    try:
        # 1. 질문 임베딩 생성
        embedding_response = ai_client.embeddings.create(
            input=query_text.replace("\n", " "),
            model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT
        )
        query_vector = embedding_response.data[0].embedding

        # 2. 벡터 쿼리 정의 (필드명: fullText_vector)
        vector_query = VectorizedQuery(
            vector=query_vector, 
            k_nearest_neighbors=top_k, 
            fields="fullText_vector" 
        )

        # 3. 검색 실행 (모든 필드 매핑 반영)
        results = search_client.search(
            search_text=None,
            vector_queries=[vector_query],
            select=[
                "id", 
                "lawName", 
                "mst", 
                "articleNo", 
                "chapterTitle", 
                "content", 
                "fullText", 
                "source", 
                "lawType"
            ]
        )

        search_results = []
        for result in results:
            search_results.append({
                "id": result.get("id"),
                "lawName": result.get("lawName"),
                "mst": result.get("mst"),
                "articleNo": result.get("articleNo"),
                "chapterTitle": result.get("chapterTitle"),
                "content": result.get("content"),
                "fullText": result.get("fullText"),
                "source": result.get("source"),
                "lawType": result.get("lawType"),
                "score": result.get("@search.score")
            })
            
        return search_results

    except Exception as e:
        print(f"검색 중 오류 발생: {str(e)}")
        return []

if __name__ == "__main__":
    # 테스트 실행
    test_query = "식품위생법상 영업 신고 절차"
    print(f"검색 테스트 시작: {test_query}")
    hits = perform_vector_search(test_query)
    
    for i, hit in enumerate(hits):
        print(f"\n[{i+1}] 법령명: {hit['lawName']} (조항: {hit['articleNo']})")
        print(f"유사도: {hit['score']:.4f}")
        print(f"내용 일부: {hit['content'][:100]}...")