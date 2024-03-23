import os
from os import path


def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value


'''
    trying to get specific input from user
    - if no corresponding input is given then 
    ask for it again.
'''


# age = get_non_negative_int("Please enter your age: ")


def check_videos_folder(folder_name):
    check_4_folder = path.exists(folder_name)

    if check_4_folder:
        print("folder exists")
    else:
        print("folder needs to be created")
        os.mkdir(folder_name)


check_videos_folder('videos')
