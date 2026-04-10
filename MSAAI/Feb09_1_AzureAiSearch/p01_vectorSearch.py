from fastapi import FastAPI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from openai import AzureOpenAI
import traceback

app = FastAPI()

# 1. 설정 정보 (Azure AI Search) - 사용자 제공 값 적용
sEndpoint = "https://choiasearchhh.search.windows.net"
sKey = "5GFdDYE4Bh23nl7ryfuRLqqW7gI9bT32tPyV6uQx3DAzSeD1B2b5"
indexName = "jobs-index"

# 2. 설정 정보 (Azure OpenAI) - 사용자 제공 값 적용
oEndpoint = "https://student02-11-1604-resource.cognitiveservices.azure.com"
oKey = "BQrdUVZyMVUpWd6Xtyvb7BAixaLikbxZlCzF5Zoj98f2pWYR6tJfJQQJ99CBACHYHv6XJ3w3AAAAACOGSqpw"
oEmbeddingDeployment = "text-embedding-3-small"

# 클라이언트 초기화
searchClient = SearchClient(sEndpoint, indexName, AzureKeyCredential(sKey))
openaiClient = AzureOpenAI(
    api_key=oKey,
    api_version="2024-02-01",  # 최신 안정 버전으로 조정
    azure_endpoint=oEndpoint,
)


def getEmbedding(text):
    """텍스트를 벡터로 변환하는 함수"""
    try:
        response = openaiClient.embeddings.create(
            input=[text], model=oEmbeddingDeployment
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"Error in getEmbedding: {str(e)}")
        raise e


@app.post("/index.data")  # 요청하신 경로로 설정
async def indexData():
    """데이터를 벡터화하여 Azure AI Search 인덱스에 업로드"""
    rawData = [
        {
            "id": "1",
            "title": "백엔드 개발자 (FastAPI)",
            "content": "Python 기반의 고성능 API 서버를 개발할 분을 찾습니다. Azure 클라우드 경험자 우대.",
            "tags": ["Python", "FastAPI", "Azure"],
        },
        {
            "id": "2",
            "title": "프론트엔드 엔지니어 (React)",
            "content": "React와 Tailwind CSS를 활용한 모던 웹 인터페이스 구축.",
            "tags": ["React", "TypeScript", "Tailwind"],
        },
        {
            "id": "3",
            "title": "프론트엔드 엔지니어 (Spring Boot)",
            "content": "Java와 Spring Boot를 활용한 웹 개발할 분 찾습니다.",
            "tags": ["React", "Spring Boot", "Java"],
        },
    ]

    processedDocuments = []
    try:
        for item in rawData:
            item["contentVector"] = getEmbedding(item["content"])
            processedDocuments.append(item)

        result = searchClient.upload_documents(documents=processedDocuments)
        return {"message": "Indexing complete", "count": len(result)}
    except Exception as e:
        errorDetails = traceback.format_exc()
        print(errorDetails)
        return {"error": str(e)}


@app.get("/vector.search")  # 요청하신 경로로 설정
async def vectorSearch(query: str):
    """의미 기반 벡터 검색 실행"""
    try:
        queryVector = getEmbedding(query)

        vectorQuery = VectorizedQuery(
            vector=queryVector,
            k_nearest_neighbors=3,
            fields="contentVector",  # Azure 포털에 설정된 필드명과 일치해야 함
        )

        results = searchClient.search(
            search_text=None,
            vector_queries=[vectorQuery],
            select=["title", "content", "tags"],
        )

        output = []
        for result in results:
            output.append(
                {
                    "title": result["title"],
                    "content": result["content"],
                    "score": result["@search.score"],
                }
            )

        return {"results": output}
    except Exception as e:
        return {"error": str(e)}
