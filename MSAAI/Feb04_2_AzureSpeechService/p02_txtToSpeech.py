from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, ResultReason
from azure.cognitiveservices.speech.audio import AudioOutputConfig

sc = SpeechConfig(
    subscription="Boz5eOExDryVTiU3oV1ttLdChUORqlhNHE2IFmflvEHNhJzxFF9LJQQJ99CBACHYHv6XJ3w3AAAYACOG6qJS",
    region="eastus2",
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
