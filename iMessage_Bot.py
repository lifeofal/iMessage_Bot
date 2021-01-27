from time import sleep
import os
from py_imessage import imessage
from random import randrange
import emoji



fullMessage = 'default'


#sets the message as an attribute

def getMessage():
    return fullMessage

# Get word from lyrics text
def get_Addontxt():
    with open('Addon.txt') as file:
        list = [line.strip() for line in file]
        string = " ".join(list)
        return string

def get_lyrics():
    with open('lyrics.txt') as file:
        list = [line.strip() for line in file]
        string = " ".join(list)
        return string


# turn text into list of words
def get_Addon(Addon_str):
    return Addon_str.split("-")
def get_words(lyrics_str):
    return lyrics_str.split("-")

# Loop through words
def send_messages(messages, phone_num, addon, numCheck):
    rand = randrange(1,8)
    rand2 = randrange(1,8)

    send_message(messages[rand], phone_num, addon[rand2], numCheck)


# Function to Send messages

# Open iMessage client

def send_message(message, phone_num, addon, numCheck):
    global fullMessage

    if bool(numCheck):
        checkBool = 1
    else:
        checkBool = 0



    os.system('osascript imessageSend.scpt "{}" "{}" {}'.format(phone_num, message + addon, checkBool))





def get_lyrics_and_send_messages(phone_num, numCheck):
    lyrics = get_lyrics()
    addon = get_Addontxt()
    words_list = get_words(lyrics)
    addon_list = get_Addon(addon)
    send_messages(words_list, phone_num, addon_list, numCheck)

