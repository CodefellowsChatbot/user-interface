import speech_recognition as sr
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            sam_speak('Sorry, I did not get that!')
        except sr.RequestError:
            sam_speak('Sorry, my speech service is down')
        return voice_data

def sam_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        sam_speak('My name is Roman')
    if 'what time is it' in voice_data:
        sam_speak(ctime())
    if 'exit' in voice_data:
        exit()


time.sleep(1)
#sam_speak('How can I help you?')
#while 1:
    #voice_data = record_audio()
    #print(voice_data)
    #respond(voice_data)