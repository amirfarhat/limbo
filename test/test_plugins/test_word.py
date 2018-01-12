import os
import sys
import requests

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(DIR, '../../limbo/plugins'))

from word import on_message
page = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt")

def test_word():
	for _ in range(20):
		ans = on_message({"text": u"!word"}, None)
		assert ans in page.text

