import wave
from piper import PiperVoice

def codificar(texto):

    voz = PiperVoice.load("voices/pt_BR-faber-medium.onnx")

    with wave.open("saida.wav", "wb") as saida:
        voz.synthesize_wav(f"{texto}", saida)

