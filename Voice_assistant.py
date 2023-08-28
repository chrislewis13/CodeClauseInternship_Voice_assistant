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
        song = instruction.replace('Play', "").strip()  
        talk("Playing " + song)
        if len(song) > 100: 
            song = song[:100]
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        print(time)
        talk('current time'+ time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        print(date)
        talk("Today's Date" + date)


    elif 'how are you' in instruction:
        talk('I am fine, how about you')

    elif 'What is your name' in instruction:
        talk('I am Python, What can I do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', "").strip()
        
        if human:
            try:
                page = wikipedia.page(human)
                info = page.summary
                print(info)
                talk(info)
            except wikipedia.exceptions.PageError:
                talk("I couldn't find information about that person.")
            except wikipedia.exceptions.DisambiguationError as e:
                first_option = e.options[0]
                page = wikipedia.page(first_option)
                info = page.summary
                print(info)
                talk(info)
        else:
            talk("Please specify a person's name after 'who is'.")
    else:
        talk("Couldn't hear you")
    
play_HeyPython()
