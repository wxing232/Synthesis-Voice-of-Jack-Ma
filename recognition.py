#!/usr/bin/env python3
# Before using google api, please make sure that you change all the "en-US" in __init__.py of speech_recognition library to "zh-CN"!!!!!!!
import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "out.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")
#AUDIO_FILE = 'E:\\jackma\\speech_recognition-master\\speech_recognition-master\\examples\\hi.wav'
# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file
result = r.recognize_google(audio)
print(result)
