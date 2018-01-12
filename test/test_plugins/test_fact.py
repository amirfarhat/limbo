import os
import sys

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(DIR, '../../limbo/plugins'))

from fact import on_message

def test_fact():
	"""
	0! = 1
	1!= 1
	5! = 120
	9! = 362880
	"""
	expected = {0:1, 1:1, 5:120, 9:362880}
	for input_value in expected:
		message = "!fact "+str(input_value)
		ans = on_message({"text": u"!fact "+str(input_value)}, None)
		assert int(ans) == expected[input_value] 

