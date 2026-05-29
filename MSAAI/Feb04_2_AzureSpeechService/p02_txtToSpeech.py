import os
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, ResultReason
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from dotenv import load_dotenv

load_dotenv()

sc = SpeechConfig(
    subscription=os.environ["AZURE_SPEECH_KEY"],
    region=os.getenv("AZURE_SPEECH_REGION", "eastus2"),
)
aoc = AudioOutputConfig(True)
sc.speech_synthesis_voice_name = "ko-KR-HyunsuNeural"
ss = SpeechSynthesizer(sc, aoc)

print("뭐 : ", end="")
txt = input()

result = ss.speak_text_async(txt).get()

if result.reason == ResultReason.SynthesizingAudioCompleted:
    print(txt)
elif result.reason == ResultReason.Canceled:
    print(result.cancellation_details)
