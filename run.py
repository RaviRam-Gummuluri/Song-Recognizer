import itertools
import threading
import time
import sys
import os
import fontstyle
import keyboard
from termcolor import colored
print(fontstyle.apply("\n\nLoading......","blink/bold/Italic/red"))

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.3)
    sys.stdout.write(colored("\r" + animation[i % len(animation)],"green"))
    sys.stdout.flush()
    
os.system('cls' if os.name == 'nt' else 'clear')
text = fontstyle.apply('Welcome to the App ! \n We offer a utility to identify song in limited time - \n\t(a) by listening to it \n\t(b) by reading from your system \nand royalty check.', 'blink/bold/Italic/red')
print(text)
time.sleep(5)
print("\n")
import tkinter as tk
import subprocess
import os
def run_program1(s):
    subprocess.run(["python", "listen.py", "-s", s])

def run_program2():
    subprocess.run(["python", "listenFromFile.py"])

def run_program3():
    subprocess.run(["python", "fingerprint.py"])

def run_program4():
    subprocess.run(["python", "reset.py"])

c=0
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(fontstyle.apply("                 MENU","bold/blue"))
    print(colored("1.Identify song from microphone","cyan"))
    print(colored("2.Identify song from Disk","cyan"))
    print(colored("3.Fingerprint the songs (preferred if any newly added)","cyan"))
    print(colored("4.Exit\n","cyan"))
    print(colored("0.Reset the database and fingerprint the songs again\n\n","red"))
    try:
        c=int(input(colored("Enter choice: ","magenta")))
    except :
        continue
    if c==1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Enter how long you want utility to listen to you (default 10 seconds):","magenta"))
        try:
            s=int(input())
        except:
            print (colored("Warning: You don't set any second. It's 10 by default", "yellow"))
            s="10"
        print(colored("\n\nrecording starts in ","yellow"))
        countdown = ["5  ","4  ","3  ","2  ","1  "]
        for i in range(len(countdown)):
            time.sleep(1)
            sys.stdout.write(colored("\r" + countdown[i % len(countdown)],"green"))
            sys.stdout.flush()
        os.system('cls' if os.name == 'nt' else 'clear')
        run_program1(str(s))
        keyboard.read_key()
        buff=input()
    elif c==2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Choose the file from your desktop.","cyan"))
        run_program2()
        keyboard.read_key()
        buff=input()
    elif c==3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Initializing fingerprinter....","red"))
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write(colored("\r" + animation[i % len(animation)],"red"))
            sys.stdout.flush()
        os.system('cls' if os.name == 'nt' else 'clear')
        run_program3()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("\nSongs fingerprinted successfully !","green"))
        keyboard.read_key()
        buff=input()
    elif c==0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Resetting database....","red"))
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write(colored("\r" + animation[i % len(animation)],"red"))
            sys.stdout.flush()
        run_program4()
        print(colored("database reset completed successfully !","green"))
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Initializing fingerprinter....","red"))
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write(colored("\r" + animation[i % len(animation)],"red"))
            sys.stdout.flush()
        os.system('cls' if os.name == 'nt' else 'clear')
        run_program3()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("\nSongs fingerprinted successfully !","green"))
        keyboard.read_key()
        buff=input()
    elif c==4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("\n\nExiting application","green"))
        for i in range(len(animation)):
            time.sleep(0.3)
            sys.stdout.write(colored("\r" + animation[i % len(animation)],"green"))
            sys.stdout.flush()
        os.system('cls' if os.name == 'nt' else 'clear')

        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Enter valid Choice !")
        sys.stdout.write
        