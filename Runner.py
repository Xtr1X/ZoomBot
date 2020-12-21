# Start

# Importing All The Modules
import sys
import time
import os
from datetime import datetime
from pynput.keyboard import Key, Controller
keyboard = Controller()

# Reading All The Text Files And Setting Up The Chats

currentpath = os.getcwd()
path = currentpath + "/Chats"
os.chdir(path)

ObjRead = open("chat1.txt", "r")
chat1 = ObjRead.read()
ObjRead = open("chat2.txt", "r")
chat2 = ObjRead.read()
ObjRead = open("chat3.txt", "r")
chat3 = ObjRead.read()
ObjRead = open("chat4.txt", "r")
chat4 = ObjRead.read()
ObjRead = open("chat5.txt", "r")
chat5 = ObjRead.read()

path = currentpath
os.chdir(path)
ObjRead = open("zoomlink.txt", "r")
zoom_link = ObjRead.read()

# Opening Up Zoom
# Get your zoom link, shorten it, and paste it below.
os.system('start ' + zoom_link)

# Waiting For Host To Accept
time.sleep(20)

# Muting Your Mic
keyboard.press(Key.num_lock)
time.sleep(4)
keyboard.press(Key.num_lock)
time.sleep(1)
keyboard.press(Key.num_lock)
time.sleep(1)
keyboard.press(Key.num_lock)

# Opening Zoom Chat
keyboard.press(Key.insert)
time.sleep(5)
keyboard.press(Key.enter)

# Sending Your Messages
keyboard.type(chat1)
keyboard.press(Key.enter)

time.sleep(7)

keyboard.type(chat2)
keyboard.press(Key.enter)

time.sleep(4)

keyboard.type(chat3)
keyboard.press(Key.enter)

time.sleep(4)

keyboard.type(chat4)
keyboard.press(Key.enter)

time.sleep(5)

keyboard.type(chat5)
keyboard.press(Key.enter)

# End



