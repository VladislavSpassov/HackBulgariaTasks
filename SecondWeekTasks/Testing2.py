import os
import sys
from pathlib import Path
from datetime import datetime

entries = Path('/home/vladislavspassov/')
#for entry in entries.iterdir():
#	print(entry.name)


#print(os.listdir('/home/vladislavspassov/Desktop/'))


basepath = '/home/vladislavspassov'

for entry in os.listdir(basepath):
    if(os.path.isfile(os.path.join(basepath,entry))):
        print(entry)

basepath = Path('/home/vladislavspassov')




with os.scandir(basepath) as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        print(info.st_mtime)


currentdir = Path(basepath)

for path in currentdir.iterdir():
    info = path.stat()
    print(info.st_mtime)
    

def convert_date(timestamp):
    d = datetime.ufcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_files():
    dir_entries = scandir(basepath)
    for d in dir_entries:
        if(entry.isfile()):
            info = entry.stat()
            print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')
        pass