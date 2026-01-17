import whisper

#Copia exata da documentação

def decodificar():
    model = whisper.load_model("small")
    audio = whisper.load_audio("entrada.wav")
    audio = whisper.pad_or_trim(audio)

    # Cria o log-mel espectograma e move para o mesmo disposotivo do modelo
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

    # Detecta a linguagem falada
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # Decodifica o áudio
    options = whisper.DecodingOptions(language="pt", fp16=False)
    result = whisper.decode(model, mel, options)

    texto = result.text
    print(texto)
    return texto
