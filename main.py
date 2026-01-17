import gravador
import ia
import tts
import playsound
import os


def main():
    #Grava o áudio
    gravador.gravar()

    #Mostra a saida
    texto_saida = ia.usar_ia()
    print(texto_saida)

    #Codifica pra voz
    tts.codificar(texto_saida)

    #fala o texto de saida da ia
    os.system("aplay saida.wav")
    
    
if __name__ == "__main__":
    main()

