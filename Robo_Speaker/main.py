import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
if __name__ == '__main__':
    print("Welcome to Robo Speaker -> Created by Rakshit")
    print("press q to quit")
    while True:
        x = input("Enter what you want me to speak: ")
        if(x=="q"):
            speak.Speak("Good Bye")
            break
        text = f"{x}"
        speak.Speak(text)




