# https://www.youtube.com/watch?v=sLiLkglsGl0&list=PLQuweJwUYMhXzZ1YxibQ3OyaYMWz8Hqam&index=33
import io
from pydub import AudioSegment
import speech_recognition as sr
import whisper_demo
import tempfile
import os
import pyttsx3
import pywhatkit
  

temp_file = tempfile.mkdtemp()
save_path = os.path.join(temp_file, 'temp.wav')
# print(f'La ruta al archivo temporal es: {save_path}')

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices') # Tomo las voces del sistema
engine.setProperty('rate', 145) # Se la ralentiza porque es muy rapida por defecto
engine.setProperty('voice', voices[2].id) # Seteo la voz en español

# Averiguar las voces instaladas
#for voice in voices :
    #print(voice)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source: # Tomo al microfono como fuente           
            print("Dia algo...")
            listener.adjust_for_ambient_noise(source) # Reduzco el ruido
            audio = listener.listen(source) # Tomo el audio
            data = io.BytesIO(audio.get_wav_data()) # Paso el audio a wav
            audio_clip = AudioSegment.from_file(data) # Tomo solo la parte donde se habla
            audio_clip.export(save_path, format='wav') # Guardo el archivo 
    except Exception as e:
        print(e)
    return save_path


def recognize_audio(save_path):
    audio_model = whisper_demo.load_model('base') # Seteo el modelo
    transcription = audio_model.transcribe(save_path, language='spanish', fp16=False)
    return transcription['text']


def main():
    try:
        response = recognize_audio(listen()).lower()
        if 'reproduce' in response:
            song = response.replace('reproduce', '')
            talk(f'Reproduciendo {song}')
            pywhatkit.playonyt(song)    
    except Exception as e:
        talk(f'Lo siento  no te entendí debido a este error: {e}')
        print(e)
    #talk(response)
    #print(response)


if __name__ == '__main__':
    main()