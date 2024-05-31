import os
import yt_dlp as youtube_dl
import optparse
import prettytable
from colorama import init, Fore, Style
import re
import requests
from sys import exit


def my_hook(d):
    if d['status'] == 'finished':
        file_tuple = os.path.split(os.path.abspath(d['filename']))
        print("\nDone downloading {}".format(file_tuple[1]))
    if d['status'] == 'downloading':
        print(f"Downloading : {d['_percent_str']}  Time Remaining : {d['_eta_str']}", end="\r")


ydl_opts = {'outtmpl': '%(title)s.%(ext)s',
            'quiet': True,
            'format': '140',
            'verbose': False,
            'postprocessors': [{'key': 'FFmpegMetadata'}],
            'progress_hooks': [my_hook],
            'cachedir' : False
            }

ydl = youtube_dl.YoutubeDL(ydl_opts)


played_ids = []




def duration_format(duration):
    return "{:02d}".format(int(duration // 60)) + " m  " +\
        "{:02d}".format(int(duration % 60)) + " s"



def play(entry):
    url = entry['webpage_url']
    played_ids.append("/watch?v=" + entry['id'])
    print(("\n{}{}" + entry['title'] +
        "{}\n").format(Style.BRIGHT, Fore.YELLOW, Style.RESET_ALL))
    os.system("mpv --no-video " + url)
    return(url)



# name = ""
# parser = optparse.OptionParser()
# parser.add_option("-s", dest="name")
# (options, arguments) = parser.parse_args()
# song_name = options.name

def main(song):
    song_name = song
    print(("\nSearching {}{}'" + song_name + "'{} on YouTube...").format(Style.BRIGHT,Fore.CYAN, Style.RESET_ALL))
    search_query = "ytsearch:" + song_name

    try:
        result = ydl.extract_info(search_query, download=False)
    except Exception as e:
        print("\nSomething is wrong.",
            "Try checking your internet connection.\n [EXCEPTION]", e)
        exit(1)
        
    url = ""
    url = play(result['entries'][0])
    
    
    
