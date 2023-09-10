from fingerprint_tools import FileReader
from termcolor import colored
from db import SQLiteDatabase
from tkinter import filedialog
import time

time.sleep(2)
fi=filedialog.askopenfilename()
if __name__ == '__main__':
  db = SQLiteDatabase()
  if fi.endswith(".mp3"):
      reader = FileReader(fi)
      audio = reader.parse_audio()
      song = db.get_song_by_filehash(audio['file_hash'])
      if song!=None:
        msg = 'Match Found, Song identified...'
        print (colored(msg, 'green') )
        msg = ' => song: %s\n'
        print (colored(msg, 'green') % (song[1]))
      else:
        msg = 'Match not found in database\nCouldnt identify song....'
        print (colored(msg, 'red'))