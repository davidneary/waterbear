# -*- coding: utf-8 -*-
import pyttsx
import json, requests
lat = raw_input("Please enter your location")
import pyowm
 
owm = pyowm.OWM('4d617acfa4c7f7673bfaa9c65a501827')
#location = raw_input("Location?")
fc = owm.daily_forecast(lat, limit=6)
f = fc.get_forecast()
f.get_location()
lst = f.get_weathers()
weather6day = []
for weather in f:
      weather6day.append(weather.get_status())
print weather6day
 
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.say('Welcome to ruff radio! A radio station able to provide vital information to secluded areas')
engine.say('The weather for the net week is as follows:')
engine.say('Day 1:')
engine.say(weather6day[0])
engine.say('Day 2:')
engine.say(weather6day[1])
engine.say('Day 3:')
engine.say(weather6day[2])
engine.say('Day 4:')
engine.say(weather6day[3])
engine.say('Day 5:')
engine.say(weather6day[4])
engine.say('Day 6:')
engine.say(weather6day[5])
engine.say('That was the weather. Now here is some information on aids and H I V and how to stop its spread')
engine.say('The Human Immunodeficiency Virus is not spread easily. You can only get HIV if you get infected blood or sexual fluids into your system.')
engine.runAndWait()
