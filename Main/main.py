from pytube import YouTube
def download_audio(url):
    audio = YouTube(url)
    audio_yt = audio.streams.get_audio_only()
    try:
        audio_yt.download()
    except ValueError:
        print("there was an error downloading your youtube video")
    print("Successful")
url = input("Input your youtube URL to get audio only: \n")
download_audio(url)
