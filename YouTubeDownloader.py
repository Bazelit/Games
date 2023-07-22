from pytube import YouTube

link = input("📎Введите url: ")
yt = YouTube(link)

stream = yt.streams.get_highest_resolution()
stream.download()

print("✅Видео скачано!")
