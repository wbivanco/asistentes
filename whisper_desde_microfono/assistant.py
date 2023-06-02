import dotenv
import os
import pywhatkit
from  modules.listen import Listener
from  modules.talk import Talk


dotenv.load_dotenv()
FAKEYOU_PASSWORD = os.getenv("FAKEYOU_PASSSWORD")

def main():
    listener = Listener()
    talker = Talk('usuario', FAKEYOU_PASSWORD, 'auronplay') # 'bob esponja'
    try:
        response = listener.listen()
        if 'reproduce' in response:
            song = response.replace('reproduce', '')
            talker.talk(f'Reproduciendo {song}')
            pywhatkit.playonyt(song)    
        #else:
            #talker.talk(response) # Reproduce lo que uno dice
    except Exception as e:
        talker.talk(f'Lo siento  no te entendí debido a este error: {e}')
        print(e)
    #talk(response)
    #print(response)


if __name__ == '__main__':
    main()
