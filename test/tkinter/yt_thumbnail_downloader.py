# Copyright 2024 kelson8 - KCNet-ThumbnailDownloader GPLV3
# Basic YouTube thumbnail downloader
# This only took me about 10 minutes to create

import requests
from pathlib import Path

# I got the idea from here: https://www.reddit.com/r/letsplay/comments/2yo1ca/guide_how_do_download_any_thumbnail_from_youtube/

# Saving image:
# https://stackoverflow.com/questions/30229231/python-save-image-from-url

# video_id = "ZFwU40K3Gbo"
# thumbnail_url = "https://img.youtube.com/vi/" + video_id + "/maxresdefault.jpg"

# Somewhat stupid way to get the video id, but it seems to work
# Get the video id from the url like this: https://img.youtube.com/vi/WN4zRCffIgE/maxresdefault.jpg
def print_video_id(url):
    video_id = url[27:38]
    print(video_id)

# print(test("https://img.youtube.com/vi/ZFwU40K3Gbo/maxresdefault.jpg"))

# Download the video thumbnail using the video id, can be obtained after the watch?v= in a YouTube link.
def download_thumbnail(video_id):
    # video_id = url[27:38]
    thumbnail_url = "https://img.youtube.com/vi/" + video_id + "/maxresdefault.jpg"

    file_name = video_id + ".jpg"
    file_path = Path(file_name)

    # https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
    # Check if the file exists, if so do nothing.
    if file_path.exists():
        print("File already exists!")
        return
    else:
        img_url = requests.get(thumbnail_url)

        # Check if the file is on the server, do nothing if there is an error.
        # https://stackoverflow.com/questions/15258728/requests-how-to-tell-if-youre-getting-a-404
        if img_url.status_code == 404:
            print("File not found!")
            return
        elif img_url.status_code == 403:
            print("Access forbidden to resource!")
            return

        img_data = requests.get(thumbnail_url).content

        with open(file_name, 'wb') as handler:
            handler.write(img_data)

        print(f"Downloaded file {file_name}.")



# I haven't completed this part of the command yet
# def video_id_input():
#     # This only takes the video id, not the url.
#     video_id_test = input("Enter the video id to download the thumbnail: ")

# def print_link():
#     print(thumbnail_url)

# def main():
#     download_thumbnail(thumbnail_url)
#
# # print_link()
#
# if __name__ == '__main__':
#     main()