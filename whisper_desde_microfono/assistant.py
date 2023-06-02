# Video 1: https://www.youtube.com/watch?v=sLiLkglsGl0&list=PLQuweJwUYMhXzZ1YxibQ3OyaYMWz8Hqam&index=33
# Video 2: https://www.youtube.com/watch?v=9IehXU1siTs&list=PLQuweJwUYMhXzZ1YxibQ3OyaYMWz8Hqam&index=33
# Error de VoiceAge: https://stackoverflow.com/questions/74668118/voiceage-error-while-using-pyttsx3-module-to-add-voice-to-statements/74727956#74727956

import pyttsx3
import pywhatkit
from  modules.listen import Listener
from  modules.talk import Talk


def main():
    listener = Listener()
    talker = Talk('usuario', 'clave', 'auronplay') # 'bob esponja'
    try:
        response = listener.listen()
        if 'reproduce' in response:
            song = response.replace('reproduce', '')
            talker.talk(f'Reproduciendo {song}')
            pywhatkit.playonyt(song)    
        else:
            talker.talk(response) # Reproduce lo que uno dice
    except Exception as e:
        talker.talk(f'Lo siento  no te entendí debido a este error: {e}')
        print(e)
    #talk(response)
    #print(response)


if __name__ == '__main__':
    main()
