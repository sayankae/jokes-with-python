import pyjokes as jk
import pyttsx3 as tts

engine = tts.init('dummy')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',rate+-20)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def joke():
  speak(jk.get_joke())
  print(jk.get_joke())

if __name__ == "__main__":
  n = int(input())
  for i in range(n):
    joke()
