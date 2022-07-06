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
# Convert it into integer(seconds)
duration_in_secs = int(duration[:2])*60*60 + int(duration[3:5])*60 + int(duration[6:])  # Improve it later

# use vlc to play the media
media_player = vlc.MediaPlayer()
media = vlc.Media(filename)
media_player.set_media(media)
media_player.play()

# Play the video for video duration length
time.sleep(duration_in_secs)