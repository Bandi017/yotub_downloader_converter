import glob
import os
import shutil
import glob

from os import path
from pytube import YouTube  # https://pytube.io/en/latest/
from moviepy.editor import *  # https://zulko.github.io/moviepy/index.html

video_id = input("Enter video is from url: ")


def get_you_tube_file(vid_id):
    yt_link = f'https://youtu.be/{vid_id}'

    YouTube(yt_link).streams.first().download()
    yt = YouTube(yt_link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print("download finished")

    get_3gpp_file = glob.glob('./*.3gpp')[0]
    print("trying to remove 3gpp file")
    if get_3gpp_file:
        os.remove(get_3gpp_file)
        print("successfully removed 3gp file")
    else:
        print("The file does not exist")


class DoesNotExist(BaseException):
    ...


def check_videos_folder(folder_name):
    check_4_folder = path.exists(folder_name)

    if check_4_folder:
        print("folder already exists")
    else:
        os.mkdir(folder_name)
        print(f"folder:{folder_name} has been created")


def change_mp4_location(prompt):
    while True:
        try:
            move_file = input(prompt).lower()
        except ValueError:
            print("Sorry, wrong input")
            continue
        get_mp4_file = glob.glob('./*.mp4')[0]
        if move_file == "yes" or move_file == 'y':
            check_videos_folder('videos')
            print("moving file")

            try:
                orig_file = get_mp4_file
                dest_file = f"./videos/{orig_file[2:]}"
                shutil.move(orig_file, dest_file)

                print("all done!!!")
                break
            except DoesNotExist as e:
                print(e)
        elif move_file == "no" or move_file == "n":
            mp4_file = get_mp4_file[2:]
            print(mp4_file)
            ask_for_mp3("convert to MP3?(yes/no)", get_mp4_file)
            break
        else:
            print("use only yes(y) or no(n): ")


def ask_for_mp3(mp3_prompt, file):
    while True:
        try:
            get_answer = input(mp3_prompt).lower()
        except ValueError:
            print("Sorry, wrong input")
            continue

        if get_answer == 'yes' or get_answer == 'y':
            convert_to_mp3(file)
            break
        elif get_answer == 'no' or get_answer == 'n':
            print("all done!!!")
            break
        else:
            print("use only yes(y) or no(n): ")


def convert_to_mp3(mp4_file):
    mp3_file_name = mp4_file[2:-3] + "mp3"
    clip = VideoFileClip(mp4_file)
    clip.audio.write_audiofile(mp3_file_name)
    print("created mp3 file and deleting original file")
    os.remove(mp4_file)


# hYh_RkkgFd0 test-video-id


get_you_tube_file(video_id)
change_mp4_location("move to videos folder? (y/n)")
