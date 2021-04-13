
import webbrowser
def open_web(query):
   if 'open youtube' in query:
        webbrowser.open("Youtube.com")
   elif 'open google' in query:
        webbrowser.open("google.com")
   elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
   elif 'open kea' in query:
        webbrowser.open("kea.kar.mic.in")
   else:
       print('sorry boss i dont know how to open it')
       print('may be you can teach me') 