import os
import tkinter as tk
from tkinter import ttk
from pytube import YouTube

def download_video():
    try:
        video_url = url_entry.get()
        yt = YouTube(video_url)
        video = yt.streams.filter(file_extension='mp4', progressive=True).first()

        download_folder = os.path.expanduser('~') + '/Downloads'
        print(download_folder)
        video.download(download_folder)

        status_label.config(text='Download Complete!')
    except Exception as e:
        status_label.config(text='Error: ' + str(e))

# Create the main window
root = tk.Tk()
root.title('YouTube Downloader')

# Create and pack widgets
url_label = ttk.Label(root, text='Enter YouTube URL:')
url_label.pack(pady=10)

url_entry = ttk.Entry(root, width=40)
url_entry.pack(pady=10)

download_button = ttk.Button(root, text='Download', command=download_video)
download_button.pack(pady=10)

status_label = ttk.Label(root, text='')
status_label.pack(pady=10)

# Start the main loop
root.mainloop()
