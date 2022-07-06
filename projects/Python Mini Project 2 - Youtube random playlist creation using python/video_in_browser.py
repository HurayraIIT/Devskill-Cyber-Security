# Abu Hurayra
import webbrowser, time

urls = ["https://www.youtube.com/watch?v=G3uclekof0c", 
        "https://www.youtube.com/watch?v=yZFrSDjRvjk",
        "https://www.youtube.com/watch?v=9RRQtNnq3s0",
        "https://www.youtube.com/watch?v=p0Q3oDY9A5s",
        "https://www.youtube.com/watch?v=woIkysZytSs"]

sleep_duration = 20 * 60    # 20 minutes

for url in urls:
  webbrowser.open(url)
  time.sleep(sleep_duration)


