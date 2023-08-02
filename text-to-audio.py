from gtts import gTTS
from playsound import playsound

def text_to_audio(text, language='en', output_file='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    playsound(output_file)

if __name__ == "__main__":
    text = input("Enter the text you want to convert to audio: ")
    text_to_audio(text)
