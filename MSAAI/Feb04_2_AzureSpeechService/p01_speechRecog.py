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
result = sr.recognize_once_async().get()

if result.reason == ResultReason.RecognizedSpeech:
    print(result.text)
elif result.reason == ResultReason.NoMatch:
    print(result.no_match_details)
elif result.reason == ResultReason.Canceled:
    print(result.cancellation_details)