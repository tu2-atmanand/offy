import pyttsx3
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(reply):
    engine.say(reply)
    engine.runAndWait()

# text = input(">")
# speak(text)













# if __name__ == '__main__':
#     count = 1
#     while count:
#         # r = sr.Recognizer()
#         # with sr.Microphone() as source:
#             # print('say something!')
#             # audio = r.listen(source, phrase_time_limit=1)
#             # print("done")
#         try:
#             # to use a wav file as a source:
#             # harvard=sr.AudioFile('file.wav')
#             # with harvard as source:
#             #     audio = r.record(source)
#
#             # to recognize directly from the microphone :
#             text = r.recognize_google(audio)
#             print('Converting\n' + text)
#             remember = open('output.txt', 'a')
#             remember.write(text+'\n')
#             if text=='exit':
#                 count=0
#         except Exception as e:
#             print(e)
#
#     remember.close()
