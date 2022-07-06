

## Step 1

Import the `pafy` module. Pafy is a python library that can download youtube content and retrieve metadata.

`> pip install pafy`

Import the `vlc` module. This module can use the functionality of the VLC Media Player. Make sure that VLC is installed in your system.

`> pip install python-vlc`

## Step 2

Import pafy and vlc. Set the url variable. Create a new pafy object with the variable and get the best quality. Then create a VLC MediaPlayer object and play the media.

```py
import pafy, vlc
url = "https://www.youtube.com/watch?v=p0Q3oDY9A5s"
video = pafy.new(url)
media = vlc.MediaPlayer(video.url)
media.play()
```

There seems to be an error.

```
PS C:\Users\huray\Documents\GitHub\Devskill-Cyber-Security\projects\Python Mini Project 2 - Youtube random playlist creation using python>                      pip install pafy
Collecting pafy
 python> python .\main.py
Traceback (most recent call last):
  File "C:\Users\huray\AppData\Local\Programs\Python\Python310\lib\site-packages\pafy\pafy.py", line 48, in <module>
    import youtube_dl
ModuleNotFoundError: No module named 'youtube_dl'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\huray\Documents\GitHub\Devskill-Cyber-Security\projects\Python Mini Project 2 - Youtube random playlist creation 
using python\main.py", line 1, in <module>
    import pafy, vlc
  File "C:\Users\huray\AppData\Local\Programs\Python\Python310\lib\site-packages\pafy\__init__.py", line 7, in <module>
    from .pafy import new
  File "C:\Users\huray\AppData\Local\Programs\Python\Python310\lib\site-packages\pafy\pafy.py", line 51, in <module>
    raise ImportError(
ImportError: pafy: youtube-dl not found; you can use the internal backend by setting the environmental variable PAFY_BACKEND to "internal". It is not enabled by default because it is not as well maintained as the youtube-dl backend.
```

I tried to install the `youtube-dl` module.

`> pip install youtube_dl`

But now a new error occurs:

```
PS C:\Users\huray\Documents\GitHub\Devskill-Cyber-Security\projects\Python Mini Project 2 - Youtube random playlist creation using python> python .\main.py
Traceback (most recent call last):
  File "C:\Users\huray\Documents\GitHub\Devskill-Cyber-Security\projects\Python Mini Project 2 - Youtube random playlist creation 
using python\main.py", line 5, in <module>
  File "C:\Users\huray\AppData\Local\Programs\Python\Python310\lib\site-packages\pafy\pafy.py", line 124, in new
    return Pafy(url, basic, gdata, size, callback, ydl_opts=ydl_opts)
    super(YtdlPafy, self).__init__(*args, **kwargs)
  File "C:\Users\huray\AppData\Local\Programs\Python\Python310\lib\site-packages\pafy\backend_shared.py", line 97, in __init__    
  File "C:\Users\huray\AppData\Local\Programs\Python\Python310\lib\site-packages\pafy\backend_youtube_dl.py", line 54, in _fetch_basic
    self._dislikes = self._ydl_info['dislike_count']
KeyError: 'dislike_count'
```

I found this [Stackoverflow article](https://stackoverflow.com/questions/70344739/backend-youtube-dl-py-line-54-in-fetch-basic-self-dislikes-self-ydl-info).

It says that youtube recently removed the dislike count from their video metadata and `pafy` library uses a variable named `dislike_count`. So until `pafy` releases an update, this issue will remain.

But there are 2 ways to solve this problem.

1. Manual Fix: You can just set the attribute _dislikes to 0 in file backend_youtube_dl.py
in Line 54: `self._dislikes = 0 # self._ydl_info['dislike_count']`
2. A pafy cloned repo has fixed this. So we can import that repo instead.

```
> pip uninstall pafy
> pip install git+https://github.com/Cupcakus/pafy
```

Now I am getting another error:

```
[000002218d3b7b20] main tls client error: connection error: Interrupted function call
[000002218d3f3480] access stream error: HTTP connection failure
```

This time I got bored after googling for a bit. The solutions did not seem clear to me.

So I decided to manually download the video and then play it from my local machine using vlc.

## Step 3

First of all let's download the video. I am downloading the worst quality to save time.

```py
import pafy, vlc, time

url = "https://www.youtube.com/watch?v=G3uclekof0c"

video = pafy.new(url)
worst_quality = video.getworst()
worst_quality.download(quiet=False)
```





Resource Credit:

1. [geeksforgeeks](https://www.geeksforgeeks.org/playing-youtube-video-using-python/)
