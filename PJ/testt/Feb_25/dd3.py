# https://raw.githubusercontent.com/h5bp/Front-end-Developer-Interview-Questions/refs/heads/main/src/translations/korean/README.md

from http.client import HTTPSConnection

from chromadb import Metadata
from ChoiStringCleaner import ChoiStringCleaner
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


# 임베딩 모델 설정
embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

# 데이터 크롤링
hc = HTTPSConnection("raw.githubusercontent.com")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

hc.request(
    "GET",
    "/h5bp/Front-end-Developer-Interview-Questions/refs/heads/main/src/translations/korean/README.md",
    headers=headers,
)

resBody = hc.getresponse().read().decode("utf-8")

hc.close()

# 데이터파싱 및 랭체인 Document 객체 생성
lines = resBody.split("\n")

tag = "General"
documents = []

for line in lines:
    line = line.strip()
    line = line.replace("**", "")
    line = line.replace("  *", "-")

    # 주제(####) 만나면 현재 태그 수정
    if line.startswith("####"):
        tag = ChoiStringCleaner.clean(line)

    # 질문(*) 만나면 현재 태그와 함께 저장
    if line.startswith("*"):
        question = ChoiStringCleaner.clean(line)

        if question:
            doc = Document(page_content=question, Metadata={"tag": tag})
        documents.append(doc)

# ChromaDB에 저장
vectorDB = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./interview_db",
    collection_name="frontendQuestion",
)

print("%s 개의 질문이 저장 되었습니다." % len(documents))