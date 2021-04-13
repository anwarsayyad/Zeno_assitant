from browsers import random_num as rd
from browsers import apps_search as asrc
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
from browsers import web as wb
import os
import time
from browsers import planning as p

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
        elif 'web' in query:
            wb.open_web(query)
        elif 'play music' in query:
            music_dir ='D:\\fun\\songs\\Music 2'
            songs = os.listdir(music_dir)
            num_songs = len(songs)
            n = rd.rand_num(num_songs)
            print('currently plalying song - ',songs[n])
            os.startfile(os.path.join(music_dir,songs[n]))
        elif 'open' in query:
            asrc.open_apps(query)
        elif 'task' in query:
           speak('do you want to add task or wanna know task ')
           nq = Takecommand().lower()
           if 'add' in nq:
               done = True
               while done:
                 speak('tell me day ')
                 r_day = Takecommand().lower()
                 if ( 'monday'or'tuesday'or 'wednesday' or 'thursday' or 'friday' or 'saturday') in r_day:

                     print(r_day)
                     day = r_day
                     done = False
                 else:
                     print(r_day)
                     speak('its not currect day please try again')
               done = True
               while done:
                    speak('tell me which time want to  your task to do')
                    r_time = Takecommand()
                    num = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24'
                    if r_time in num:
                         print(r_time)
                         time = int(num)
                         done =False
                    else:
                         speak('sorry please say in numbers')
               done = True
               while  done:
                    speak('please tell me what is your task')
                    r_task = Takecommand().lower()
                    print(r_task)
                    speak(r_task)
                    speak('you want to save this task ')
                    rep_1 = Takecommand()
                    if 'yes' in rep_1:
                        task = r_task 
                        done = False
               done = True
               while done:
                    speak('do you have any important work    ')
                    rep_1 = Takecommand().lower()
                    if 'yes' in rep_1:
                        r_imp = Takecommand().lower()
                        print(r_imp)
                        print('you want to save your important task ? please reply in yes or no')
                        res = Takecommand().loewr()
                        if 'yes' in res:
                            imp = r_imp
                            done = False
                        elif 'no' in rep_1:
                            imp = ''
                        else:
                            speak('please say it again i cant understand ')

                
           elif 'know' in nq:
               pass 
           else:
               speak('sorry boss you need to say add  for adding task and know if wanna know your task ')
                
        elif 'quit' in query:
            exit() 
        time.sleep(5)    