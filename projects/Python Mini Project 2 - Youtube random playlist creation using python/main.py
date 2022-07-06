import pafy, vlc, time

url = "https://www.youtube.com/watch?v=G3uclekof0c"

video = pafy.new(url)
worst_quality = video.getworst()

# Download the video
filename = worst_quality.download(quiet=False, filepath="name." + worst_quality.extension)
print(filename)

# Get video duration
duration = video.duration
print(duration) # 00:00:44

# use vlc to play the media
media_player = vlc.MediaPlayer()
media = vlc.Media(filename)
media_player.set_media(media)
media_player.play()

# Find the duration of the video in integer and play the video for that duration
# 00:00:44 to 44
time.sleep(int(duration[:2])*60*60 + int(duration[3:5])*60 + int(duration[6:]))