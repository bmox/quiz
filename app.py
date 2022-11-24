#read a json file


from rich.console import Console
console = Console()

import os
from time import sleep
import pyglet
from gtts import gTTS

def play_audio(audio_file):
    music = pyglet.media.load(audio_file, streaming=False)
    music.play()
    sleep(music.duration)
    
def google_tts(mytext,speed):
    tts = gTTS(text=mytext,tld="ca", lang="en",slow=speed)
    filename = './audio/temp.mp3'
    tts.save(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    sleep(music.duration)
    os.remove(filename)   
    
import speech_recognition as sr
r = sr.Recognizer()
def speech_to_text(filename):
    file = filename
    with sr.AudioFile(file) as source:
        audio_listened = r.listen(source)
        try:
            result = r.recognize_google(audio_listened)
            # print("You said : {}".format(result))
            
        except sr.UnknownValueError:
            result="None"
    return result
        
        
import sounddevice
import soundfile
def record_audio(second):
    file_name="./audio/output.wav"
    fs= 44100
    second =  second
    console.print("@ Recording.....n",style="Bold Red")
    record_voice = sounddevice.rec( int ( second * fs ) , samplerate = fs , channels = 2 )
    sounddevice.wait()
    soundfile.write(file_name, record_voice, fs, subtype='PCM_16')
    console.print("Finished.....",style="Bold Red")     
    stt=speech_to_text(file_name) 
    return stt

wrong_count=0
def check_ans(user_ans):
    global wrong_count
    my_prediction= [f"option {ans}", answer.lower()]
    for k in answer.lower().split(" "):
        if len(k)>2:
            my_prediction.append(k.replace(" ", ""))
    flag=True
    # print("user_ans:",user_ans)
    # print("my_prediction:",my_prediction)
    for  m in my_prediction:
        if m in user_ans:
            console.print(f"Your are right . option {ans} {answer}" , style="Bold Yellow")
            google_tts(f"Your are right . option {ans} {answer}",False)
            flag=False
            break
    if flag!=False:
        wrong_count+=1
        console.print(f"You are wrong . option {ans}. {answer} is the correct answer",style="Bold Red")
        google_tts(f"You are wrong . option {ans}. {answer} is the correct answer",False)
        if wrong_count>5:
            play_audio("./audio/wrong.mp3")
            wrong_count=0

        
import json
import random
console.print("Welcome to the quiz game",style="Bold Green")
console.print("1. Assignment 1",style="Bold Green")
console.print("2. Assignment 2",style="Bold Green")
console.print("Enter the assignment number:",style="Bold Green")
which=input()
if which=="1":
    path="./data/1.json"
elif which=="2":
    path="./data/2.json"
else:
    console.print("Invalid input",style="Bold Red")
    exit()
with open(path) as f:
# with open('./data/1.json') as f:
    data = json.load(f)
    random.shuffle(data)
    play_audio("./audio/intro.mp3")
    for i in data:
        q_no=i['q_no']
        question = i['data']['question']
        a=i['data']['a']
        b = i['data']['b']
        c=i['data']['c']
        d=i['data']['d']
        ans= i['data']['answer']
        answer= i['data'][ans]
        console.print(f"{q_no}. {question}",style="Bold Green")
        console.print("\ta:",a,style="Bold Green")
        console.print("\tb:",b ,style="Bold Green")
        console.print("\tc:",c  ,style="Bold Green")
        console.print("\td:",d  ,style="Bold Green")
        # print("\tAnswer:",ans)
        console.print("what is your answer?",style="Bold Blue")
        
        speak_test=f"Question number {q_no}. {question} . option a. {a}. option b. {b}. option c. {c}. option d. {d}."
        # print(speak_test) 
        google_tts(speak_test,False)
        google_tts("what is the answer?" ,False)
        user_ans=record_audio(5)
        
        user_ans=user_ans.lower()
        console.print("user_ans:",user_ans,style="Bold Purple")
        pre=["repeat","repeat the question","the question","question"]
        for p in pre:
            if p in user_ans:
                
                google_tts(speak_test,False)
                google_tts("what is the answer?",False)
                user_ans=record_audio(5)
                user_ans=user_ans.lower()
        check_ans(user_ans)
        
            
                    
           
             
