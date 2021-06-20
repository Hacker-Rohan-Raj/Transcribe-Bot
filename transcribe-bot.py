import speech_recognition as sr
print('''

 _______                            _ _                        ____        _   
|__   __|                          (_) |                      |  _ \      | |  
   | |_ __ __ _ _ __  ___  ___ _ __ _| |__   ___ ______ ______| |_) | ___ | |_ 
   | | '__/ _` | '_ \/ __|/ __| '__| | '_ \ / _ \______|______|  _ < / _ \| __|
   | | | | (_| | | | \__ \ (__| |  | | |_) |  __/             | |_) | (_) | |_ 
   |_|_|  \__,_|_| |_|___/\___|_|  |_|_.__/ \___|             |____/ \___/ \__|
                                                                               
                                                                               ''')
print('--------------------------------------------------------------------------')
print('-------------------------Made by Hacker--Rohan Raj------------------------')
print('---------------------------No.1 Transcribe Bot----------------------------')
print('--------------------------------------------------------------------------')
print('Please enter Your File Name which is located in this directory \n')
filename = input()

print(sr.__version__)
r = sr.Recognizer()
print('Proceeding... Please Wait')
file_audio = sr.AudioFile (filename)

with file_audio as source:
   audio_text = r.record(source)


print(type(audio_text))
print(r.recognize_google(audio_text))
Print('File Transcribed')