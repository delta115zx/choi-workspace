# pip install azure-cognitiveservices-speech
import os
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, ResultReason
from azure.cognitiveservices.speech.audio import AudioConfig
from dotenv import load_dotenv

load_dotenv()

sc = SpeechConfig(
    subscription=os.environ["AZURE_SPEECH_KEY"],
    region=os.getenv("AZURE_SPEECH_REGION", "eastus2"),
)
sc.speech_recognition_language = "ko-KR"

ac = AudioConfig(True)
sr = SpeechRecognizer(sc, ac)

print("말 : ")
result = sr.recognize_once_async().get()

if result.reason == ResultReason.RecognizedSpeech:
    print(result.text)
elif result.reason == ResultReason.NoMatch:
    print(result.no_match_details)
elif result.reason == ResultReason.Canceled:
    print(result.cancellation_details)