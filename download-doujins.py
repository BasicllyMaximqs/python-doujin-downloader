import nhentai
import os
import urllib
import time
import shutil
from os import path
from shutil import copyfile


_startint = 0

_global_limit = 999999

_check_for_loli = True

def main_menu():
    global _check_for_loli
    print("[?] Download Specific Doujin (y/n)? Default: False")
    yesno = input()
    if yesno == "y":
        download_specific_doujin()
    else:
        print("[?] Set your Doujin #. Limit (Ur Starting from 1 but checks will be done to avoid dupes):")
        _global_inputreq = input()
        _global_limit = _global_inputreq
        
        print("[?] Include tag 'loli/lolicon' (y/n)? Default: False | by downloading lolicon doujins you might incriminate yourself depending on your country's laws.")
        _quick_input = input()
        
        if _quick_input == "y":
            _check_for_loli = False
        else:
            _check_for_loli = True
            
        loop_downloader()

def download_specific_doujin():
    doujin_id_temp = input("Doujin ID:" )
    
    print(f"[!] Attempting to get Doujin ({doujin_id_temp})")
    
    doujin_try = nhentai.get_doujin(doujin_id_temp)
        
    if path.exists(doujin_try.titles["english"]):
        print("[!] Dupe Found -- Quitting!")
        exit()
            
    os.mkdir(f"[{doujin_id_temp}] {doujin_try.titles['english']}")
    shutil.copyfile("index.php", f"./[{doujin_id_temp}] {doujin_try.titles['english']}/index.php")
    _custom_length = len(doujin_try.pages)
    
    for x in range(1, _custom_length):
        if x > _custom_length:
            print("[!] Download Complete")
            exit()
                
        print(f"[!] Downloading Page {x} from: {doujin_try.titles['english']}")
        urllib.request.urlretrieve(doujin_try[x].url, f"./[{doujin_id_temp}] {doujin_try.titles['english']}/{str(x)}.png")
    exit()

def loop_downloader():
    global _startint
    global _global_limit
    while _startint < _global_limit:
        _startint = _startint + 1
        print(f"[!] Waiting 2 Seconds for #{_startint}")
        time.sleep(2)
        start_download()

    print("[!] Finished Download")


def start_download():
    #main declare
    _doujin = nhentai.get_doujin(_startint)
    
    print("[!] Checking for dupes..")
    
    if path.exists(f"[{_startint}] {_doujin.titles['english']}"):
        print("[!] Dupe Found -- Skipping!")
        return;
    
    print(f"[!] Preparing download for ID {_startint}")

    # loli check
    
    _length_loli_check = len(_doujin.tags)
    
    is_loli = False
    if _check_for_loli:
        for tag_content in range(1, _length_loli_check):
            if tag_content == _length_loli_check:
                break;
            
            if _doujin.tags[tag_content].type == "tag":
                if _doujin.tags[tag_content].name == "lolicon":
                    is_loli = True
                    break;
                else:
                    print(f"[!] Ignored non-Loli tag ({_doujin.tags[tag_content].name})")
            else:
                print(f"[!] Ignored non-tag object ({str(_length_loli_check)})")

    if is_loli:
        print(f"[!] Loli Doujin was removed from list: ({_doujin.titles['english']})")
    else:
        download_doujin(_startint)
        
def download_doujin(_id):
    print(f"[!] Starting Download of ID {_id} - Preparing")
    
    _doujin_temp = nhentai.get_doujin(_id)
    
    print(f"[!] Making Title directory: {_doujin_temp.titles['english']}")
    os.mkdir(f"[{_id}] {_doujin_temp.titles['english']}")
    print(f"[!] Making Index: {_doujin_temp.titles['english']}")
    shutil.copyfile("index.php", f"./[{_id}] {_doujin_temp.titles['english']}/index.php")
    
    _doujin_pages_length = len(_doujin_temp.pages)
    
    for x in range(1, _doujin_pages_length):
        if x > _doujin_pages_length:
            print(f"[!] Doujin {_doujin_temp.titles['english']}) was downloaded!")
            break;
        
        print(f"[!] Downloading Page {x} from: {_doujin_temp.titles['english']}")
        urllib.request.urlretrieve(_doujin_temp[x].url, f"./[{_id}] {_doujin_temp.titles['english']}/{x}.png")
        
        
    print(f"[!] Downloading of '{_doujin_temp.titles['english']}' Complete!")
    
print("Python Doujin Downloader - Written by BasicllyMaximqs\n[!] Warning: Root is required.")
main_menu()
    
    
