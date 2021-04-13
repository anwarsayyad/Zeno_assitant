import os
def open_apps(query):
    if 'open bluestacks' in query:
        bpath = "C:\\Program Files\BlueStacks\Bluestacks.exe"
        os.startfile(bpath)
    elif 'open telegram' in query:
        bpath = "C:\\Users\\anwar\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
        os.startfile(bpath)
    elif 'open chrome' in query:
        bpath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        os.startfile(bpath)
    else:
        print('sorry i was not able to find it please try diffrent one ')