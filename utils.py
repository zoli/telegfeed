import datetime

def date_format(message):
    if type(message) is datetime:
        return message.strftime("%Y-%m-%d %H:%M:%S")
