import pyaudio
import wave
import constantes
import os
import sys

#Tirar incompatibilidade do alsa e jack
devnull = os.open(os.devnull, os.O_WRONLY)
os.dup2(devnull, sys.stderr.fileno())

def gravar():
    audio = pyaudio.PyAudio()   

    #Tirado da documentação
    stream = audio.open(
        input=True,
        format= constantes.FORMAT,
        channels= constantes.CHANNELS,
        rate= constantes.RATE,
        frames_per_buffer= constantes.CHUNK
    )

    frames = []

    print("GRAVANDO...")
    try:
        while True:
            bloco = stream.read(constantes.CHUNK)
            frames.append(bloco)
    except KeyboardInterrupt:
        pass
        print("\nEncerrado")
    
    stream.stop_stream()
    stream.close()
    audio.terminate()

    #Cria o arquivo entrada.wav
    with wave.open("entrada.wav", "wb") as entrada:
        entrada.setnchannels(constantes.CHANNELS)
        entrada.setframerate(constantes.RATE)
        entrada.setsampwidth(audio.get_sample_size(constantes.FORMAT))
        entrada.writeframes(b"".join(frames))


