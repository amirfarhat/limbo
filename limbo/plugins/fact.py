"""!fact calculates the factorial of a number."""
import re

def factorial(n):
    if type(n) != int or n < 0: 
        return None
    if n in {0, 1}:
        return 1
    else: 
        return n * factorial(n-1)

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!fact( .*)?", text)
    if not match:
        return
    return str(factorial(int(match[0])))

on_bot_message = on_message
