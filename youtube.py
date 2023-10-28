from pytube import YouTube
link = 'https://www.youtube.com/watch?v=x7AurjpuZGA'
youtube_1 = YouTube(link)
#print(youtube_1.title)
#print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input('Enter a number = '))
videos[strm].download()
print('Successfully')
