#!/usr/bin/python3

import datetime
import random
import sys
import time
import webbrowser


def set_alarm(hour, minute, am_pm):
    now = datetime.datetime.now()
    hour = hour - abs(now.hour) % 12
    if now.hour <= 12 and am_pm == 'PM':
        hour += 12
    if now.hour > 12 and am_pm == 'AM':
        hour += 12
    minute = minute - now.minute
    time_set = datetime.timedelta(hours=hour, minutes=minute).seconds
    return time_set


hour = 0
minute = 0
am_pm = ''
if sys.argv:
    for arg in sys.argv:
        if '--hour' in arg:
            hour = int(arg.split('=')[-1])
        if '--minute' in arg:
            minute = int(arg.split('=')[-1])
        if '--period' in arg:
            am_pm = arg.split('=')[-1]
        if '-h' == arg:
            print('usage: alarm_clock.py\nparameters: --hour=<hours>\n\
            --minute=<minutes>\n\
            --period=<AM/PM>')
            sys.exit(1)

with open('youtube_playlist.txt', 'r') as f:
    urls = f.readlines()

alarm = set_alarm(hour, minute, am_pm)
t = datetime.datetime.now() + datetime.timedelta(seconds=alarm)

print('Alarm set: %s' % t.strftime('%I:%M %p'))

time.sleep(alarm)

webbrowser.open(random.choice(urls))
