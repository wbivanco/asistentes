# https://www.youtube.com/watch?v=SL6qw9-9NEQ
import whisper
import pandas as pd


# Selección y carga del modelo (en este caso "medium")
model = whisper.load_model("medium")
# Transcripción del audio a un diccionario
result = model.transcribe("killers.mp3", fp16=False)
# Impresión del resultado de la transcripción
print(result["text"])
# Guardo en dataframe los segmentos del audio y selecciona el campo segmento del resultado
# pd.DataFrame(result["segments"])