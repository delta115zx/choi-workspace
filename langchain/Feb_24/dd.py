import os
import json
from langchain_community.document_loaders import GitLoader

class InterviewScraper:
    def __init__(self):
        # 수집된 데이터를 저장할 리스트
        self.all_documents = []
        # 대상 저장소 정보 (실제 clone을 통해 데이터를 가져옵니다)
        self.repos = [
            {
                "clone_url": "https://github.com/gyoogle/tech-interview-for-developer",
                "repo_path": "./repos/gyoogle",
                "branch": "master"
            },
            {
                "clone_url": "https://github.com/JaeYeopHan/Interview_Question_for_Beginner",
                "repo_path": "./repos/jbee",
                "branch": "master"
            }
        ]

    def fetch_with_langchain(self):
        """LangChain의 GitLoader를 사용하여 저장소의 모든 .md 파일을 로드합니다."""
        for repo in self.repos:
            print(f"📦 {repo['clone_url']} 로딩 중...")
            
            # GitLoader는 로컬에 저장소를 복제(clone)한 뒤 파일을 읽어옵니다.
            loader = GitLoader(
                clone_url=repo["clone_url"],
                repo_path=repo["repo_path"],
                branch=repo["branch"],
                file_filter=lambda file_path: file_path.endswith(".md") # 마크다운 파일만 필터링
            )
            
            # 문서 로드 (Document 객체 리스트 반환)
            docs = loader.load()
            print(f"✅ {len(docs)}개의 마크다운 파일을 확보했습니다.")
            
            for doc in docs:
                # 메타데이터와 내용을 정리하여 저장
                self.all_documents.append({
                    "source": doc.metadata.get("source"),
                    "category": doc.metadata.get("file_name"),
                    "content": doc.page_content
                })

    def save_results(self):
        """수집된 데이터를 JSON으로 저장합니다."""
        with open("interview_documents.json", "w", encoding="utf-8") as f:
            json.dump(self.all_documents, f, ensure_ascii=False, indent=4)
        print(f"✨ 전체 {len(self.all_documents)}개의 문서 세그먼트 저장 완료.")

if __name__ == "__main__":
    # 필수 라이브러리 설치 안내: pip install GitPython langchain_community
    scraper = InterviewScraper()
    
    print("🚀 LangChain GitLoader 기반 파이프라인 시작...")
    scraper.fetch_with_langchain()
    scraper.save_results()

# [중요 포인트]
# 1. GitLoader를 쓰면 정규식으로 일일이 링크를 찾을 필요가 없습니다.
# 2. 로컬에 clone된 파일을 직접 읽으므로 속도가 훨씬 빠르고 안정적입니다.
# 3. doc.page_content에 마크다운 내용이 통째로 들어있어, 이후 텍스트 분할(Splitter)이 용이합니다.