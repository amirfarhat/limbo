"""!word produces a random word in English"""

import requests
import random
import re

def get_random_words(num_words = 1):
	page = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt")
	text = page.text.split()
	return random.choice(text)

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!word( .*)?", text)
    if not match:
        return
    return get_random_words()

on_bot_message = on_message
