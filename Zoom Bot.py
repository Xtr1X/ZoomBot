# Importing Basic Modules

import sys
import time
import os
from datetime import datetime

# Installing Advanced Modules
os.system('title Initializing...')
print("Initializing")
time.sleep(.6)
os.system('cls')
print("Initializing.")
time.sleep(.6)
os.system('cls')
print("Initializing..")
time.sleep(.6)
os.system('cls')
print("Initializing...")
time.sleep(.6)
print()
print()
print()
os.system('pip install colorama')
os.system('pip install pynput')
os.system('cls')

# Importing Colorama
import colorama
from colorama import Fore, Back, Style



# Getting Current Time
now = datetime.now()
current_time = now.strftime("%H:%M")

# GUI 1
os.system('title Zoom Bot - By: Sam')
print(Fore.CYAN + "  ______                           ____        _   ")
print(" |___  /                          |  _ \      | |  ")
print("    / / ___   ___  _ __ ___       | |_) | ___ | |_ ")
print("   / / / _ \ / _ \| '_ ` _ \      |  _ < / _ \| __|")
print("  / /_| (_) | (_) | | | | | |     | |_) | (_) | |_ ")
print(" /_____\___/ \___/|_| |_| |_|     |____/ \___/ \__|")
print()
print(Fore.RED + "                       By: Sam")
print(Fore.GREEN + "               Beta v1.0 | Opensource")
print()
print()
print()
print(Fore.WHITE + "Current Time: " + current_time)
print()
print(Fore.LIGHTGREEN_EX + "What time does your zoom start? | Please use military time.")
print()
print(Fore.BLUE + "Format: HOUR:MINUTE")
print()

# Getting Your Input
zoom_time = input(Fore.RED + '-=- ')

# GUI 2
os.system('cls')
print(Fore.RED + 'Initializing')
time.sleep(.6)
os.system('cls')
print(Fore.RED + 'Initializing.')
time.sleep(.6)
os.system('cls')
print(Fore.RED + 'Initializing..')
time.sleep(.6)
os.system('cls')
print(Fore.RED + 'Initializing...')
time.sleep(.6)
os.system('cls')
print(Fore.RED + 'Initializing')
time.sleep(.6)
os.system('cls')
print(Fore.RED + 'Initializing.')
time.sleep(.6)
os.system('cls')
print(Fore.RED + 'Initializing..')
time.sleep(.6)
os.system('cls')
print(Fore.RED + 'Initializing...')
time.sleep(.6)

os.system('cls')
print()
print(Fore.MAGENTA + "         ,--.   ,--.        ,--.  ,--.  ,--.                            ")
print("         |  |   |  | ,--,--.`--',-'  '-.`--',--,--,  ,---.              ")
print("         |  |.'.|  |' ,-.  |,--.'-.  .-',--.|      \| .-. |             ")
print("         |   ,'.   |\ '-'  ||  |  |  |  |  ||  ||  |' '-' '.--..--..--. ")
print("         '--'   '--' `--`--'`--'  `--'  `--'`--''--'.`-  / '--''--''--' ")
print("                                                    `---'               ")
print(Fore.WHITE + "                          Joining Zoom At " + zoom_time + " !")
print()
print(Fore.LIGHTRED_EX + "Simply keep this window, along with the zoom application open and enjoy sleeping in!")


# Loop / Checking the time every second until it matches the input, then running the runner.py
count = 0
while (count < 1 ): 
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if zoom_time==current_time:
        os.system('Runner.py')
        count = count + 1
    else:
        count = count + 0
