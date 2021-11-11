import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source_audio:
    print("Say the words you want recognized now:")
    captured_audio = recognizer.listen(source_audio)
    

try:
    print("Google Speech Recognition heard " + recognizer.recognize_google(captured_audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand what you said")
   
   
#based on https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
#did not hear me well at low volumes, but accuracy seems alright