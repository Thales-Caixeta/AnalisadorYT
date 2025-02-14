import os
import openai
import ffmpeg
from pytubefix import YouTube
import time

openai.api_key = os.getenv("OPENAI_API_KEY")  

def baixar_audio(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    output_file = audio_stream.download(filename="video_audio.mp4")

    audio_path = "video_audio.wav"
    ffmpeg.input(output_file).output(audio_path, format="wav").run(overwrite_output=True)


    os.remove(output_file)
    return audio_path

def transcrever_audio(audio_path):
    with open(audio_path, "rb") as audio_file:
        try:
            response = openai.Audio.transcribe("whisper-1", audio_file)
            os.remove(audio_path)  
            return response["text"]
        except openai.error.RateLimitError:
            print("\u26a0\ufe0f Erro: Cota da API excedida. Tente novamente mais tarde.")
            return None
        except Exception as e:
            print(f"\u26a0\ufe0f Erro na transcrição: {e}")
            return None

def resumir_texto(texto):
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Resuma o seguinte texto:"},
                {"role": "user", "content": texto}
            ]
        )
        return resposta["choices"][0]["message"]["content"]
    except openai.error.RateLimitError:
        print("\u26a0\ufe0f Erro: Cota da API do GPT-4 excedida.")
        return None
    except Exception as e:
        print(f"\u26a0\ufe0f Erro ao gerar resumo: {e}")
        return None

def main():
    url = input("Digite a URL do vídeo do YouTube: ")

    print("Baixando áudio...")
    audio_path = baixar_audio(url)

    print("Transcrevendo áudio...")
    texto_transcrito = transcrever_audio(audio_path)

    if texto_transcrito:
        print("\nResumo do vídeo:")
        resumo = resumir_texto(texto_transcrito)
        if resumo:
            print(resumo)
            with open("resumo.txt", "w", encoding="utf-8") as f:
                f.write(resumo)
            print("\nResumo salvo em 'resumo.txt'.")
        else:
            print("Não foi possível gerar o resumo.")
    else:
        print("Não foi possível transcrever o áudio.")

if __name__ == "__main__":
    main()
