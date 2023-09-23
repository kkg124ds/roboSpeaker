import  gtts    ## google text to speech
import  playsound
print("Welcome to Robospeaker 1.1 created by kamal")
while True:

    text = input("say something here: ")
    if text == "q":
        break

    sound=gtts.gTTS(text,lang="en")
    sound.save("welcome.mp3")
    playsound.playsound("welcome.mp3")