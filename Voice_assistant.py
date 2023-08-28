import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listner = aa.Recognizer()


machine = pyttsx3.init()

def talk (text):
    machine.say(text)
    machine.runAndWait()


def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech = listner.listen(origin)
            instruction = listner.recognize_google(speech)
            instruction = instruction.lower()
            if "heypython" in instruction:
                instruction = instruction.replace('heypython', "")
                print(instruction)

    except:
        pass
    return instruction




def play_HeyPython():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('Play', "").strip()  # Remove leading/trailing spaces
        talk("Playing " + song)
        if len(song) > 100:  # Truncate the song if it's too long
            song = song[:100]
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('current time'+ time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's Date" + date)


    elif 'how are you' in instruction:
        talk('I am fine, how about you')

    elif 'What is your name' in instruction:
        talk('I am Python, What can I do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', "")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)



    else:
        talk("Couldn't hear you")

play_HeyPython()
