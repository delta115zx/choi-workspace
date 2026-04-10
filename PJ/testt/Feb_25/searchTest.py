from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

# 기존 저장된 ChromaDB로드
vectorDB = Chroma(
    persist_directory="./interview_db",
    embedding_function=embeddings,
    collection_name="frontendQuestion",
)

userInput = input("사용자의 기술 스택을 입력해주세요 (예: React, JavaScript) : ")
techStack = []

userInput = userInput.split(",")
for tech in userInput:
    techStack.append(tech)

result = []

for tech in techStack:
    # 각 기술 별로 2개 검색
    results = vectorDB.similarity_search_with_score(tech, k=2)
    result.append((tech, results))

# print(result)

# 중복 질문을 방지하기 위한 집합(set)과 순번(count) 관리
seenQuestions = set()
count = 1

for tech, group in result:
    print("%s 관련 추천 질문" % tech)
    for doc, score in group:
        if doc.page_content not in seenQuestions:
            tag = doc.metadata.get("tag", "General")
            # 점수는 낮을수록 유사도가 높음(거리)
            print(
                "%s.  [%s]    %s  (유사도: %s) \n"
                % (count, tag, doc.page_content, score)
            )
            seenQuestions.add(doc.page_content)
            count += 1
