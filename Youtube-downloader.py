from pytube import YouTube
import os


def dl_video(url, path):
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    if not os.path.exists(path):
        os.makedirs(path)
    stream.download(path)
    print('Download finished')


if __name__ == "__main__":
    my_url = input('Please enter the URL:')
    my_path = input('Please enter the path on your computer:')
    dl_video(my_url, my_path)
