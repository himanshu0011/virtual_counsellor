def speak(text):
     import pyttsx3
     engine = pyttsx3.init()
     engine.say(text)
     engine.runAndWait()
    
import speech_recognition as sr
print("Hey")
speak("Hey")
r= sr.Recognizer()
r.dynamic_energy_threshold=0

with sr.Microphone() as source:
     r.pause_threshold=1
     r.adjust_for_ambient_noise(source)
     print("...")
     audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    
     command=r.recognize_google(audio)
     print("You said: " +command )
except sr.UnknownValueError:
     print("Google Speech Recognition could not understand audio")
    
print("Who are you")
speak("Who are you")
r= sr.Recognizer()
r.dynamic_energy_threshold=0

with sr.Microphone() as source:
     r.pause_threshold=1
     r.adjust_for_ambient_noise(source)
     print("...")
     audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    
     command1=r.recognize_google(audio)
     print("You said: " +command )
except sr.UnknownValueError:
     print("Google Speech Recognition could not understand audio")
     
print("How can i help you "+command1)
speak("How can i help you "+command1)     

r= sr.Recognizer()
r.dynamic_energy_threshold=0

with sr.Microphone() as source:
     r.pause_threshold=1
     r.adjust_for_ambient_noise(source)
     print("...")
     audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    
     command1=r.recognize_google(audio)
     print("You said: " +command )
except sr.UnknownValueError:
     print("Google Speech Recognition could not understand audio")
     
print("Okay answer some question")
speak("Okay answer some question") 
r= sr.Recognizer()
r.dynamic_energy_threshold=0

with sr.Microphone() as source:
     r.pause_threshold=1
     r.adjust_for_ambient_noise(source)
     print("...")
     audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    
     command1=r.recognize_google(audio)
     print("You said: " +command )
except sr.UnknownValueError:
     print("Google Speech Recognition could not understand audio")
     
print("What will you do in your leisure time")
speak("What will you do in your leisure time") 

r= sr.Recognizer()
r.dynamic_energy_threshold=0

with sr.Microphone() as source:
     r.pause_threshold=1
     r.adjust_for_ambient_noise(source)
     print("...")
     audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    
     command2=r.recognize_google(audio)
     print("You said: " +command2)
except sr.UnknownValueError:
     print("Google Speech Recognition could not understand audio")
     
print("What you are currently doing")
speak("What you are currently doing")
r= sr.Recognizer()
r.dynamic_energy_threshold=0

with sr.Microphone() as source:
     r.pause_threshold=1
     r.adjust_for_ambient_noise(source)
     print("...")
     audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    
     command3=r.recognize_google(audio)
     print("You said: " +command3)
except sr.UnknownValueError:
     print("Google Speech Recognition could not understand audio")

if (command3=="10th Standard" or command3=="12th standard" or command3=="11th standard"):
    print("Which Stream you want to take or in which stream you are? ")
    speak("Which Stream you want to take or in which stream you are? ")    
    r= sr.Recognizer()
    r.dynamic_energy_threshold=0

    with sr.Microphone() as source:
     r.pause_threshold=1
     r.adjust_for_ambient_noise(source)
     print("...")
     audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
    try:
     stream=r.recognize_google(audio)
     print("You said: " +stream)
    except sr.UnknownValueError:
     print("Google Speech Recognition could not understand audio")
    
     
    