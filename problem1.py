# Twinkle Twinkle poem

print('''Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!
Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!''')

# Print table of 5

print(f'''
      5 x 1  = {5*1}
      5 x 2  = {5*2}
      5 x 3  = {5*3}
      5 x 4  = {5*4}
      5 x 5  = {5*5}
      5 x 6  = {5*6}
      5 x 7  = {5*7}
      5 x 8  = {5*8}
      5 x 9  = {5*9}
      5 x 10 = {5*10}
''')

# User External Module to perform operation of your interest 
# ! Text to Speech (TTS) library for Python 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.

import pyttsx3
engine = pyttsx3.init()
engine.say('''Hello Engine is working fine ''')
engine.runAndWait()

#! write a python program to print content of a directory using os module 

import os

def list_directory_contents(path):
    try:
        # List all the files and directories in the given path
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")

# Specify the directory path you want to list
directory_path = '/Hataf/Python Programming/PythonProgramming2024'  # '.' means the current directory

list_directory_contents(directory_path)





