# 최진영 · 개발 학습 포트폴리오

> AI/클라우드 백엔드 개발자를 목표로 학원 과정 및 자기주도 학습을 기록한 저장소입니다.

---

## 목차

1. [소개](#소개)
2. [기술 스택](#기술-스택)
3. [개인 프로젝트](#개인-프로젝트)
4. [학습 기록](#학습-기록)
5. [주요 성과 (SOHOBI)](#주요-성과-sohobi)

---

## 소개

학원 커리큘럼(Python → 웹개발 → 머신러닝/딥러닝 → Azure AI)을 이수하면서 쌓은 실습 코드와,
그 과정에서 독립적으로 개발한 개인 프로젝트를 함께 관리하는 저장소입니다.

학습 폴더는 날짜 기반 폴더명(`Nov17_1_HTML`, `Jan22_1_Text` 등)으로 체계적으로 정리되어 있으며,
각 프로젝트는 실제 데이터·API를 사용한 실전 경험을 담고 있습니다.

---

## 기술 스택

| 영역 | 기술 |
|------|------|
| **AI / Azure** | Azure OpenAI (GPT-4o), Azure AI Search, Semantic Kernel, Azure ML |
| **Backend** | Python 3.12, FastAPI, Flask, Node.js, REST API, JWT |
| **Frontend** | React 19, Vite, Tailwind CSS, Redux, JavaScript, Socket.IO |
| **Database** | PostgreSQL, Oracle DB, MongoDB, CosmosDB, ChromaDB |
| **Infra** | Azure Container Apps, Azure Blob Storage, Docker, Linux, GitHub Actions |
| **Data / ML** | NumPy, Pandas, Matplotlib, Seaborn, scikit-learn, PyTorch, TensorFlow, KoNLPy |

---

## 개인 프로젝트

### 1. 포트폴리오 웹사이트 (`portfolio.jsx` + `portfolio-socket-srv/`)

> React 19 기반 인터랙티브 포트폴리오 페이지

- **기술:** React 19, Vite, Socket.IO, Node.js, Express
- **주요 기능:**
  - 방문자 실시간 카운트 (Socket.IO `visitor_count` 이벤트)
  - 방문자 간 협업 드로잉 보드 — 캔버스 마우스 좌표를 소켓으로 실시간 브로드캐스트
  - 기술 스택, 프로젝트, 문제 해결 사례 섹션 구성
- **특이사항:** 서버 미연결 시에도 UI가 정상 동작하도록 소켓 연결 실패를 graceful하게 처리

---

### 2. 상권분석 에이전트 (`CHOI/locationAgent/`)

> Azure OpenAI + Semantic Kernel 기반 자연어 상권 조회 에이전트

- **기술:** Python, Semantic Kernel 1.40, Azure OpenAI, SQLite, Pandas
- **기능:** 자연어 질의 → 동 단위·상권 단위 매출/점포 분석
  - 9개 지역, 12개 업종 지원
  - Function Calling 기반 플러그인 구조로 분석 도구 확장

---

### 3. 음식점 업종 분류기 (`CHOI/locationAgent_DB/db/`)

> 공공데이터 API + 상호명 기반 업종 세부 분류 스크립트

| 파일 | 설명 |
|------|------|
| `fetch_sclscode.py` | 소상공인 상가정보 API로 서울시 음식업종 소분류 코드 페이지네이션 수집 (429 재시도 포함) |
| `type_classifier.py` | 상호명 키워드 매칭으로 분식·양식을 14/9개 세부 타입으로 분류, 행정동별 집계 및 미보유 타입 탐지 |

- **데이터 출처:** 공공데이터포털 소상공인 상가정보 API (`apis.data.go.kr`)
- **입력 데이터:** 서울특별시 일반음식점 CSV (`식품_일반음식점_서울특별시.csv`)

---

### 4. 법령 벡터 검색 (`CHOI/vectorSearch/`)

> 생활법령 문서를 Azure AI Search에 인덱싱하는 전처리 파이프라인

- **기술:** Python, Azure AI Search, text-embedding-3-large
- **내용:** 식품위생법·근로기준법 등 법령 JSON 전처리 → 임베딩 생성 → 하이브리드 인덱스 적재
- **활용:** SOHOBI 법령 RAG 에이전트의 데이터 파이프라인 기반

---

## 학습 기록

### Python 기초 (`python/`)

기초 문법부터 OOP·예외처리·파일I/O·DB 연동까지 단계별 실습.

| 폴더 예시 | 주제 |
|-----------|------|
| `Oct07_1_variable` | 변수, 자료형 |
| `Oct14_1_function` | 함수, 스코프 |
| `Nov04_1_OOP` | 클래스, 상속, 다형성 |
| `Nov11_1_exception` | 예외 처리, 파일 I/O |
| `Nov18_1_DB` | Oracle DB 연동, SQL |

---

### 웹 개발 기초 (`web/`)

HTML/CSS 마크업부터 Flask·FastAPI 백엔드, Node.js, WebSocket 채팅까지.

| 폴더 예시 | 주제 |
|-----------|------|
| `Nov17_1_HTML` | HTML 구조, 시맨틱 태그 |
| `Nov25_1_CSS` | CSS 레이아웃, Flexbox |
| `Dec02_1_jQuery` | DOM 조작, 이벤트 |
| `Dec08_4_Chat` | WebSocket 채팅 (학원 채팅 패턴의 원형) |
| `Jan05_1_Flask` | Flask REST API |
| `Jan12_1_FastAPI` | FastAPI, Pydantic |
| `Jan19_1_NodeJS` | Node.js, Express |

---

### 웹 개발 심화 (`newWeb/`)

ES6+, React 생태계, 인증/인가, 비동기 통신 심화.

| 폴더 예시 | 주제 |
|-----------|------|
| `Feb02_1_ES6` | ES6+ 문법 (화살표함수, 구조분해, Promise) |
| `Feb09_1_React` | React 컴포넌트, 훅 |
| `Feb16_1_Redux` | Redux 상태관리 |
| `Feb23_1_JWT` | JWT 인증, Refresh Token |
| `Mar02_1_AJAX` | AJAX, Axios, fetch API |
| `Mar09_1_FileUpload` | 멀티파트 파일 업로드 |

---

### 데이터 분석 & AI (`BDAI/`)

NumPy · Pandas · 시각화 → 머신러닝 전 과정 실습.

| 폴더 예시 | 주제 |
|-----------|------|
| `Jan22_1_Text` | 텍스트 전처리, 정규표현식 |
| `Feb05_1_NumPy` | 배열 연산, 브로드캐스팅 |
| `Feb12_1_Pandas` | DataFrame, 그룹연산 |
| `Feb19_1_Visual` | Matplotlib, Seaborn 시각화 |
| `Mar05_1_ML` | scikit-learn 분류/회귀 |
| `Mar19_1_Cluster` | 비지도학습, K-Means |

---

### 머신러닝 / 딥러닝 (`MSAML/`)

PyTorch CNN, TensorFlow, NLP, 이미지 처리, 추천 시스템까지 Jupyter Notebook 50+ 실습.

주요 주제: `CNN 이미지 분류`, `감성 분석`, `시계열 예측`, `협업 필터링 추천`

---

### Azure AI 서비스 (`MSAAI/`)

Azure Cognitive Services 전 영역 Python 실습 (~20개 파일).

| 서비스 | 실습 내용 |
|--------|-----------|
| Azure OpenAI | GPT-4o, DALL-E 3 이미지 생성 |
| Computer Vision | 객체 탐지, OCR, 이미지 분석 |
| Speech | STT / TTS |
| Translator | 다국어 번역 |
| Language | NER, Sentiment Analysis, Key Phrase |

---

### LangChain / 벡터 DB (`langchain/`)

Chroma DB 로컬 벡터 저장소와 LLM 통합 실습.

- `chroma_basic/` — 문서 임베딩 저장·조회
- `chroma_qa/` — RAG 기반 질의응답
- `chroma_persist/` — 영구 저장소 관리

---

## 주요 성과 (SOHOBI)

> 이 저장소에 코드가 포함되지 않는 팀 프로젝트이나, 핵심 기술 경험으로 기재합니다.
> 별도 GitHub 레포지토리에서 관리 중입니다.

**SOHOBI** — F&B 창업자 대상 멀티에이전트 AI 플랫폼 (라이브 서비스 중 · sohobi.net)

| 항목 | 내용 |
|------|------|
| 팀 규모 | 4인 팀 (MS SAY 2-2) |
| 개발 기간 | 2026년 2월 25일 ~ 4월 10일 (6주) |
| 실사용자 | 약 80명 |
| GitHub 활동 | 커밋 770건, Merged PR 255건 |

**담당 기술 기여:**

- **멀티에이전트 아키텍처** — Semantic Kernel 기반 오케스트레이터 + 5개 도메인 에이전트 설계
- **Sign-off 검증 시스템** — 33개 루브릭 코드, 최대 3회 자동 재처리
- **RAG 파이프라인** — 법령 1,288개 조항 / 정부지원사업 5,600건 하이브리드 검색 (HNSW + BM25 + 시맨틱 리랭킹)
- **성능 최적화** — 응답 레이턴시 32.7초 → 11.9초 (-63.6%), 상권분석 46.5초 → 11.2초 (-75.9%)
**기술 스택:** FastAPI · Semantic Kernel · Azure OpenAI (GPT-4o) · Azure AI Search · React 19

---

*문의: delta115zx@gmail.com*
