import pafy, vlc

url = "https://www.youtube.com/watch?v=3cHOljTssGo"
video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlayer(best.url)
media.play()
