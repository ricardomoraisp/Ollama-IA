import whisper

#Copia exata da documentação

def decodificar():
    model = whisper.load_model("small")
    audio = whisper.load_audio("entrada.wav")
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions(language="pt", fp16=False)
    result = whisper.decode(model, mel, options)

    texto = result.text
    print(texto)
    return texto
