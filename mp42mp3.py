from moviepy.editor import *
# https://zulko.github.io/moviepy/index.html
import glob

get_mp4_file = glob.glob('./*.mp4')

mp4_file_name = get_mp4_file[0]
mp3_file_name = mp4_file_name[2:-3] + "mp3"

print(mp3_file_name)

clip = VideoFileClip(mp4_file_name)
clip.audio.write_audiofile(mp3_file_name)
