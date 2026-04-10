# Choi Workspace

개인 학습 및 프로젝트 통합 워크스페이스입니다.
Python (AI/ML/Data), JavaScript/Node.js (웹 프론트엔드), Java 기반 다양한 프로젝트를 포함합니다.

---

## 폴더 구조

| 폴더 | 설명 |
|------|------|
| `BDAI/` | 데이터 분석 학습 (NumPy, Pandas — 지하철, 타이타닉 등) |
| `CHOI/` | AI 오케스트레이션 프로젝트 (FastAPI, Semantic Kernel, 벡터 검색, locationAgent) |
| `MSAAI/` | Azure AI 서비스 통합 (OpenAI, Computer Vision, Speech, Translator) |
| `MSAML/` | ML 학습 (Jupyter Notebook, PyTorch, NLP) |
| `PJ/` | 프로젝트 (Semantic Kernel, 상권 분석, 벡터 검색) |
| `SOHOBI/` | 팀 협업 프로젝트 (FastAPI + Semantic Kernel + React, 4인 협업) |
| `langchain/` | LangChain 학습 및 RAG 구현 (Chroma DB) |
| `locationAgent/` | 위치 기반 상권 분석 에이전트 (FastAPI, Semantic Kernel) |
| `newWeb/` | Node.js 웹 프로젝트 모음 (Vite, React, Vue, Redux, Socket.io) |
| `python/` | Python 실습 (XML/JSON 파싱, HTTP 통신, Oracle DB) |
| `web/` | HTML + jQuery 웹 실습 (AJAX, 지리정보, 모바일 웹) |
| `java/` | Java 프로젝트 (Eclipse 기반) |
| `lib/` | 커스텀 유틸리티 라이브러리 (JS: 유효성 검사 / Python: DB·파일·문자열 처리) |
| `잡/` | 메모, 학습 자료, CSV 데이터 |

---

## 외부 라이브러리 Requirements

이 저장소에는 포함되지 않은 외부 라이브러리입니다. 별도로 다운로드하여 프로젝트 루트에 배치하세요.

### JavaScript 라이브러리

| 라이브러리 | 버전 | 설치 방법 |
|------------|------|-----------|
| [bxSlider](https://bxslider.com) | 4.2.17 | `npm install bxslider` 또는 [GitHub](https://github.com/stevenwanderski/bxslider-4/releases/tag/4.2.17) 에서 다운로드 |
| [CanvasJS Chart](https://canvasjs.com) | 3.14.9 | [canvasjs.com](https://canvasjs.com/download-html5-charting-library/) 에서 다운로드 |
| [CanvasJS StockChart](https://canvasjs.com) | 1.14.9 | [canvasjs.com](https://canvasjs.com/download-html5-charting-library/) 에서 다운로드 |

### Python 의존성

각 프로젝트 폴더의 `requirements.txt` 참고:

```bash
# 예시 (각 프로젝트 폴더에서 실행)
pip install -r requirements.txt
```

주요 Python 패키지:
- `semantic-kernel` 1.40.0
- `langchain`
- `fastapi`
- `openai`
- `azure-identity`
- `pandas`, `numpy`
- `torch` (PyTorch)

### 환경변수 설정

각 프로젝트 폴더의 `.env.example`을 복사하여 `.env`로 만들고 값을 채워넣으세요:

```bash
cp .env.example .env
```
