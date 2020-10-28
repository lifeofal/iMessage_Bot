from time import sleep
import os
from py_imessage import imessage
from random import randrange
import emoji


num = "7704024415‬"
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
def send_messages(messages, phone_num, addon):
    rand = randrange(1,8)
    rand2 = randrange(1,8)

    send_message(messages[rand], phone_num, addon[rand2])
    print(rand)
    print(rand2)
    print(emoji.emojize(':thumbs_up:'))

# Function to Send messages

# Open iMessage client

def send_message(message, phone_num, addon):

    os.system('osascript send.scpt {} "{}"'.format(phone_num, emoji.emojize('Go DAWGS')))


def get_lyrics_and_send_messages(phone_num, lyrics, addon):
    words_list = get_words(lyrics)
    addon_list = get_Addon(addon)
    send_messages(words_list, phone_num, addon_list)

for x in range(200):
    get_lyrics_and_send_messages(num, get_lyrics(), get_Addontxt())