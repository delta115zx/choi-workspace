from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

key = "ERkMkD4YKfCZ0em4iNk2aECd7bYoS7v0QF9i6P8ZS5YwTdXcrZLPJQQJ99CBACYeBjFXJ3w3AAAFACOG8WEO"
endpoint = "https://choicvvv.cognitiveservices.azure.com/"
iac = ImageAnalysisClient(endpoint, AzureKeyCredential(key))

f = open("C:/Choi/menu.png", "rb")
imgData = f.read()

cvResult = iac.analyze(
    image_data=imgData,
    visual_features=[
        VisualFeatures.CAPTION,
        VisualFeatures.OBJECTS,
        VisualFeatures.PEOPLE,
        VisualFeatures.READ,
    ],
)

# 이미지 주제 찾기
# print("caption")
# if cvResult.caption is not None:
#     print(cvResult.caption.text, cvResult.caption.confidence)
# print("-----")
cap = ""
if cvResult.caption is not None:
    cap = cvResult.caption.text
# # 객체
# print("object")
# if result.objects is not None:
#     print(result.objects)

# # 사람
# print("caption")
# if result.people is not None:
#     print(result.people)
# print("-----")

txt = ""
# OCR
print("read")
if cvResult.read is not None:
    for line in cvResult.read.blocks:
        for t in line["lines"]:
            txt += t["text"]
print("-----")


# pip install azure-ai-translation-text==1.0.0b1
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

key = "6eoOH0cGTDtr3TDzwrJ43ZS2bOd4hQaxE0Nvk2c5UKXW4xvfj5aIJQQJ99CBACHYHv6XJ3w3AAAbACOGZfhm"
endpoint = "https://api.cognitive.microsofttranslator.com/"
region = "eastus2"

tc = TranslatorCredential(key, region)
ttc = TextTranslationClient(credential=tc, endpoint=endpoint)
targetLang = ["ko"]

itis = [InputTextItem(text=cap), InputTextItem(text=txt)]

res = ttc.translate(content=itis, to=targetLang)
# print(res)
tCap = res[0]["translations"][0]["text"]
tTxt = res[1]["translations"][0]["text"]

# pip install azure-cognitiveservices-speech
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, ResultReason
from azure.cognitiveservices.speech.audio import AudioConfig


sc = SpeechConfig(
    subscription="6tH4fnGnFe97L67g9DozhOCYhW1z0KhB9vn7aRh3NF35IeeQwlrWJQQJ99CBACHYHv6XJ3w3AAAYACOGBujn",
    region="eastus2",
)
sc.speech_recognition_language = "ko-KR"

ac = AudioConfig(True)
sr = SpeechRecognizer(sc, ac)

print("말 : ")
srResult = sr.recognize_once_async().get()

if srResult.reason == ResultReason.RecognizedSpeech:
    print("내가 한 말 : ", srResult.text)
# elif srResult.reason == ResultReason.NoMatch:
#     print(srResult.no_match_details)
# elif srResult.reason == ResultReason.Canceled:
#     print(srResult.cancellation_details)


from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, ResultReason
from azure.cognitiveservices.speech.audio import AudioOutputConfig

sc = SpeechConfig(
    subscription="6tH4fnGnFe97L67g9DozhOCYhW1z0KhB9vn7aRh3NF35IeeQwlrWJQQJ99CBACHYHv6XJ3w3AAAYACOGBujn",
    region="eastus2",
)
aoc = AudioOutputConfig(True)
sc.speech_synthesis_voice_name = "ko-KR-HyunsuNeural"
ss = SpeechSynthesizer(sc, aoc)

# print("뭐 : ", end="")
if srResult.reason == ResultReason.RecognizedSpeech:
    if "주제" in srResult.text:
        txt = tCap
    elif "내용" in srResult.text:
        txt = tTxt

scResult = ss.speak_text_async(txt).get()

if scResult.reason == ResultReason.SynthesizingAudioCompleted:
    print("답변 내용 : ", txt)
elif scResult.reason == ResultReason.Canceled:
    print(scResult.cancellation_details)
