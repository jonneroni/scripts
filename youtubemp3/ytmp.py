"""Download youtube video as mp3
    Run script after copying a video url to clipboard
"""


import win32clipboard
import yt_dlp as yt


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

    if isEffect == "y":
        output = "K://Äänet//efektit//{}".format(filename)
    else:
        output = "K://Äänet//muut//{}".format(filename)

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
