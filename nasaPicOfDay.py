# Lots of code stolen from https://www.youtube.com/watch?v=VLNcnROUTb8&t=428s&ab_channel=PythonEngineer
# Modified by Sam Silver

import requests
import pwd
import os
import ctypes
from sys import platform

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
FILENAME = 'nasa_pic.png'


def check_config():
    # Opens config to get folder to track
    if os.path.exists("NasaConfig.txt"):
        file = open("NasaConfig.txt", "r")
        folder = file.read()
        file.close()
    else:  # If file does not exist then make one!
        print("No config file found...")
        folder = input(
            "Where would you like me to store the NASA images: ")

        while not(os.path.exists(folder)):  # Make sure the entered dir exists
            folder = input(
                "That path does not exist... please re-enter:")

        print("Creating config...\n")

        file = open("NasaConfig.txt", "w")
        file.write(folder)
        file.close
    return folder + "/" + FILENAME


def download_pic():
    request = requests.get(url)
    if request.status_code != 200:
        print('ERROR')
        return

    picture_url = request.json()['url']
    if "jpg" not in picture_url:
        print("No image for today, must be a video")
    else:
        pic = requests.get(picture_url, allow_redirects=True)
        filename = check_config()

        open(filename, "wb").write(pic.content)

        print(f"Saved the pic of the day to {filename}!")


if __name__ == '__main__':
    download_pic()

    filename = check_config()

    # set background
    if platform == "linux":
        cmd = "gettings set org.gnome.desktop.background picture-uri file:" + filename
        os.system(cmd)
    elif platform == "darwin":
        cmd = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" + filename + "\"'"
        os.system(cmd)
    elif platform == "win32":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, filename, 0)
