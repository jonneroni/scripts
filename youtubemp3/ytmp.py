import win32clipboard
import yt_dlp as yt
from tkinter.filedialog import askdirectory
from tkinter import *
import json
import os


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def startupCheck():
    if os.path.isfile(os.path.join(__location__, 'setup.json')):
        pass
    else:
        with open(os.path.join(__location__, 'setup.json'), 'w') as db_file:
            db_file.write(json.dumps({"effectDir": "", "otherDir": ""}))


def readJson():
    return json.loads(open(os.path.join(__location__, 'setup.json')).read())


def writeJson(file):
    with open(os.path.join(__location__, 'setup.json'), "w") as f:

        json.dump(file, f, indent=4)


startupCheck()

cacheJson = readJson()

effectFolderNotSet = cacheJson["effectDir"] == ""
otherFolderNotSet = cacheJson["otherDir"] == ""

if effectFolderNotSet:
    path = askdirectory(title='Select effect folder')
    cacheJson["effectDir"] = path
    writeJson(cacheJson)

if otherFolderNotSet:
    path = askdirectory(title='Select folder for others')
    cacheJson["otherDir"] = path
    writeJson(cacheJson)


# get clipboard data
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
print(data)

try:
    video_info = yt.YoutubeDL().extract_info(
        url=data, download=False
    )

    isEffect = input("Onko ääniefekti? (y/n): ")

    nameInput = input("Syötä tiedostonimi, tyhjä jos automaattinen\n")
    if nameInput == "":
        filename = f"{video_info['title']}.mp3"
    else:
        filename = f"{nameInput}.mp3"

    setupJson = readJson()

    if isEffect == "y":
        output = '{}//{}'.format(setupJson["effectDir"], filename)
    else:
        output = '{}//{}'.format(setupJson["otherDir"], filename)

    options = {
        'format': 'm4a/bestaudio/best',
        'keepvideo': False,
        'outtmpl': output,
    }

    with yt.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(filename))


except Exception as e:
    print(e)
