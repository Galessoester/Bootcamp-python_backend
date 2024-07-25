import os

import speech_recognition as sr

print("testando...")

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)

        print("Diga alguma coisa...")
        
        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google_cloud(audio, language='pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")
            return False
        
        elif "Excel" in frase:
            os.system("start Excel.exe")
            return False
        
        elif "fechar" in frase:
            os.system("exit")
            return True

        print("Voce disse " + frase)
    except sr.UnknownValueError:
        print("não entendi.")
    
    return frase

while True:
    if ouvir_microfone():
        break