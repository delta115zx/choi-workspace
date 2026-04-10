from azure.cognitiveservices.speech import ResultReason
from azure.cognitiveservices.speech.audio import AudioConfig
from azure.cognitiveservices.speech.translation import (
    SpeechTranslationConfig,
    TranslationRecognizer,
)

stc = SpeechTranslationConfig(
    subscription="Boz5eOExDryVTiU3oV1ttLdChUORqlhNHE2IFmflvEHNhJzxFF9LJQQJ99CBACHYHv6XJ3w3AAAYACOG6qJS",
    region="eastus2",
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
