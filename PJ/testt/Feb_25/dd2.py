# https://raw.githubusercontent.com/h5bp/Front-end-Developer-Interview-Questions/refs/heads/main/src/translations/korean/README.md

from http.client import HTTPSConnection

from ChoiStringCleaner import ChoiStringCleaner


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

lines = resBody.split("\n")

tag = "General"
interviewData = []

for line in lines:
    line = line.strip()
    line = line.replace("**", "")

    # 주제(####) 만나면 현재 태그 수정
    if line.startswith("####"):
        tag = ChoiStringCleaner.clean(line)

    # 질문(*) 만나면 현재 태그와 함께 저장
    if line.startswith("*"):
        question = ChoiStringCleaner.clean(line)

        if question:
            data = {"question": question, "tag": tag}
        interviewData.append(data)

print(interviewData[:30])