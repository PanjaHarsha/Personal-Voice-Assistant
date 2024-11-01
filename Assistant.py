import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    """
This method will allow Alexa to speak, It take our voice as an argument
    """
    engine.say(audio)
    engine.runAndWait()


def greetUser():
    """
This method will always greet the user in start.
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 11:
        speak("Good Morning!")

    elif hour >= 11 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your Personal voice assistant. Please tell me how may I help you?")


def takeCommand():
    """
    It takes microphone input from the user and returns string output, return None in case of any problem
    """

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("how can I help?")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-UK')
        print(f"User said: {query}\n")
        

    except Exception as e:
        # print(e)    hiding error from console
        print("Speak it again please...")
        return "None"
    return query


if __name__ == "__main__":
    greetUser()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'who is' in query:
          person = query.replace('who is','')
          info = wikipedia.summary(person,1)
          print(info)
          speak(info)    

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'who created you' in query:
          speak('D 2 group Panja HarshaVardhan, Patha Rahul, Nallapati Ankith Chowdary, Paidi AjayVardhan ')      

        elif 'play' in query:
          song = query.replace('play','')
          speak('playing' + song)
          pywhatkit.playonyt(song)

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            
        elif 'open college website' in query:
            webbrowser.open("https://www.bharathuniv.ac.in/")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            codePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)

        elif 'open git' in query:
            codePath = "C:\\Program Files\\Git\\git-bash.exe"
            os.startfile(codePath)

        elif 'quit' or 'shut' in query:
            speak("Thanks for giving me your time")
            exit()
