
# 🎥 Resumo de Vídeos do YouTube com OpenAI 🎬

## 🚀 Visão Geral

Este projeto tem como objetivo **extrair áudio de vídeos do YouTube**, transcrevê-lo usando a API **Whisper** da OpenAI e gerar um **resumo inteligente** com o **GPT-4**. O resumo gerado é salvo em um arquivo de texto para facilitar o acesso e a leitura.

---

## 🛠️ Tecnologias Utilizadas

- **pytubefix**: Para baixar o áudio dos vídeos do YouTube.
- **ffmpeg**: Para converter o áudio em formato adequado para transcrição.
- **OpenAI Whisper**: Para transcrever o áudio em texto.
- **OpenAI GPT-4**: Para gerar um resumo do texto transcrito.
- **Python**: Linguagem principal do projeto.

---

## 📦 Como Usar

### 1. Instalar Dependências

Primeiro, instale as bibliotecas necessárias executando o comando abaixo:

```bash
pip install openai ffmpeg pytubefix
```

### 2. Configuração da API da OpenAI

Defina sua chave de API da OpenAI como uma variável de ambiente:

- No **Windows**:

```bash
setx OPENAI_API_KEY "sua-chave-aqui"
```

- No **Linux/macOS**:

```bash
export OPENAI_API_KEY="sua-chave-aqui"
```

### 3. Executar o Script

Após a configuração, execute o script com o seguinte comando:

```bash
python script.py
```

O programa pedirá a URL de um vídeo do YouTube e, ao final do processo, gerará um resumo que será salvo no arquivo `resumo.txt`.

---

## ⚙️ Como Funciona

- Baixa o áudio de um vídeo do YouTube.
- Converte o áudio para o formato WAV adequado para transcrição.
- Transcreve o áudio usando o Whisper da OpenAI.
- Gera um resumo do texto transcrito utilizando o GPT-4.
- Salva o resumo no arquivo `resumo.txt`.

---

## 🔧 Melhorias Futuras

- Criar uma interface web (usando **Flask** ou **Streamlit**).
- Salvar a transcrição e o resumo em um banco de dados.
- Ajustar o tamanho do resumo conforme a preferência do usuário.
- Adicionar suporte para diferentes idiomas.
- Melhorar o tratamento de erros e exceções.

---

## ⚠️ Desafios

- Erros de transcrição podem ocorrer devido à qualidade do áudio.
- Limites da API da OpenAI podem afetar o uso gratuito.
- O tempo de processamento pode ser alto para vídeos longos.

---



# 🌐 English Version

## 🚀 Overview

This project allows you to download audio from YouTube videos, transcribe it using OpenAI's Whisper API, and generate an intelligent summary with GPT-4. The generated summary is saved in a text file for easy access and reading.

---

## 🛠️ Technologies Used

- **pytubefix**: To download audio from YouTube videos.
- **ffmpeg**: To convert audio into a suitable format for transcription.
- **OpenAI Whisper**: To transcribe audio into text.
- **OpenAI GPT-4**: To generate a summary from the transcribed text.
- **Python**: Main programming language of the project.

---

## 📦 How to Use

### 1. Install Dependencies

First, install the required libraries by running the following command:

```bash
pip install openai ffmpeg pytubefix
```

### 2. Set Up the OpenAI API Key

Set your OpenAI API key as an environment variable:

- On **Windows**:

```bash
setx OPENAI_API_KEY "your-key-here"
```

- On **Linux/macOS**:

```bash
export OPENAI_API_KEY="your-key-here"
```

### 3. Run the Script

After configuring the API, run the script with this command:

```bash
python script.py
```

The program will ask for a YouTube video URL, and at the end of the process, it will generate a summary saved in the `resumo.txt` file.

---

## ⚙️ How It Works

- Downloads audio from a YouTube video.
- Converts audio into WAV format for transcription.
- Transcribes audio using OpenAI's Whisper.
- Generates a summary of the transcribed text using GPT-4.
- Saves the summary in the `resumo.txt` file.

---

## 🔧 Future Improvements

- Create a web interface (using **Flask** or **Streamlit**).
- Save transcription and summary to a database.
- Allow users to adjust the summary length.
- Add support for different languages.
- Improve error handling and exceptions.

---

## ⚠️ Challenges

- Transcription errors may occur due to audio quality.
- OpenAI API limits may affect usage.
- Processing time may be long for large videos.

---
