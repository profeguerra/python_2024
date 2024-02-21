from pytube import YouTube

url = 'https://www.youtube.com/watch?v=L7dBplP_PfM'

#print(url)

youtube = YouTube(url)

stream = youtube.stream.get_highest_resolution()

download_path = '/home/linux/Development/Python/course_2401/python_2024/022024'
file_name = '40 day - Dave B.mp4'
stream.download(download_path, file_name)