#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import speech_recognition as sr
import time
import os
import numpy as np
from os import path

def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

path = 'E:\\jackma\\sliced\\'
files = os.listdir(path)
r = sr.Recognizer()
for file in files[:3]:
# use the audio file as the audio source
    #time.sleep(3)
    with sr.AudioFile(path+file) as source:
        audio = r.record(source)  # read the entire audio file
    # recognize speech using Microsoft Bing Voice Recognition
    BING_KEY = "BING_KEY"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    try:
        result = r.recognize_bing(audio, key=BING_KEY)
        save_to_file(file[:10]+'.txt', result)
    except:
        print('failed')
