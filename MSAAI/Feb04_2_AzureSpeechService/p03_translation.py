import os
from azure.cognitiveservices.speech import ResultReason
from azure.cognitiveservices.speech.audio import AudioConfig
from azure.cognitiveservices.speech.translation import (
    SpeechTranslationConfig,
    TranslationRecognizer,
)
from dotenv import load_dotenv

load_dotenv()

stc = SpeechTranslationConfig(
    subscription=os.environ["AZURE_SPEECH_KEY"],
    region=os.getenv("AZURE_SPEECH_REGION", "eastus2"),
)
stc.speech_recognition_language = "ko-KR"
stc.add_target_language("en")
stc.add_target_language("ja")
ac = AudioConfig(True)
tr = TranslationRecognizer(stc, audio_config=ac)

print("말 : ")
result = tr.recognize_once_async().get()

if result.reason == ResultReason.TranslatedSpeech:
    print(result.text)
    print(result.translations["en"])
    print(result.translations["ja"])
elif result.reason == ResultReason.NoMatch:
    print(result.no_match_details)
elif result.reason == ResultReason.Canceled:
    print(result.cancellation_details)
