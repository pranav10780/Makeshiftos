"""this is the main prog that takes input from usr and sends it to the appropriate config files"""
from config import handler
while True:
    data = input('#:')
    handler.recievedata(data)
