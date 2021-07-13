import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


engine = pyttsx3.init()
#engine.say('Hello, I am Troy')
#engine.say('How can i help you?')
#engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        listener = sr.Recognizer()
#       listener.adjust_for_ambient_noise(source,duration=5)
        listener.energy_threshold=4000
        
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'Troy' in command:
                command=command.replace('Troy','')
                print(command)
    except:
        pass
    return command

def run_Troy():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        print(song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I %M %p')
        talk('The time is' + time)
        print(time)

    elif 'information' in command:
        fact=command.replace('Information','')
        info=wikipedia.summary(fact,5)
        print(info)
        talk(info)

    elif 'jokes' in command:
        talk(pyjokes.get_joke())

    elif 'who are you' in command:
        talk('I am Troy, a test trial of Alexa built by Keleigh Berenger. I was born in September. I am very smart and I love Micheal Jackson')

    elif 'are you single' in command:
        talk('I just love God, thats all')

    else:
        talk('Sorry, i did not understand. Can you please repeat what you said')

while True:
    run_Troy()