import io
from pydub import AudioSegment
import speech_recognition as sr
import whisper
import tempfile
import os

temp_file = tempfile.mkdtemp()
save_path = os.path.join(temp_file, 'temp.wav')
# print(f'La ruta al archivo temporal es: {save_path}')

listener = sr.Recognizer()


class Listener:
    def __listen_from_mic(self): 
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


    def __recognize_audio(self, save_path):
        audio_model = whisper.load_model('base') # Seteo el modelo
        transcription = audio_model.transcribe(save_path, language='spanish', fp16=False)
        return transcription['text']
    
    def listen(self):
        return self.__recognize_audio(self.__listen_from_mic()).lower()