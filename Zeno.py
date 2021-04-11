from browsers.random_num import rand_num
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<6:
        speak('good night!!')
        speak('Boss. its too late you should sleep now ')
    elif hour>=6 and hour<9:
        speak('oh! boss awesome you woke up ealy good mornig!!!')
        speak('how can i help you')
    elif hour>=9 and hour<12:
        speak('damn boss you woke up late today harry up!!!')
    elif hour>=12 and hour<18:
        speak('good afternoon boss. how can i help you.')
    elif hour>=18 and hour<22:
        speak('hey boss!! how is your day today what are you looking for') 
    else:
        speak('well its night boss are you planning to rest??')
def Takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listing.....')
        r.pause_threshold = 1 
        r.energy_threshold = 300

        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-IN')
        print(f"user said :{query}\n")
    except Exception as e:
        print('say that again please....')
        return 'None'
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = Takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia .....')
            query= query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif ('what is your name' or 'who are you') in query:
            speak('I am your beloved assistant  Zeno!!!!') 
        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir ='D:\\fun\\songs\\Music 2'
            songs = os.listdir(music_dir)
            num_songs = len(songs)
            n = rand_num(num_songs)
            print('currently plalying song - ',songs[n])
            os.startfile(os.path.join(music_dir,songs[n]))

        elif 'quit' in query:
            exit() 
        time.sleep(10)    