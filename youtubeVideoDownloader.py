# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "P:/"

# link of the video to be downloaded
link = "https://youtu.be/Ke90Tje7VS0"

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error")  # to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.filter("mp4")

# to set the name of the file
yt.set_filename("React Video")

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
d_video.download(SAVE_PATH)
print("Task Completed!")
