import pyttsx3
import scipy as sp
import speech_recognition as sr

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        answer = r.recognize_google(audio, language='en-US')
        print(answer)
    
    except Exception as e:
        print(e)
        print("Say that again please!")
        return "None"
    return answer


speak("What's your name?")
name = take_command()
print("Welcome "+name+" to this adventure!")
speak("Welcome "+name+" to this adventure!")

print("Do you want to play?")
speak("Do you want to play?")
play = take_command()

while 'yes' in play:

    print("You are in a dark forest. You are walking. It has come to an end. You can see a mountain. And you can go left or right. Which way would you like to go? Left, right or do you wanna climb the mountain?\n")
    speak("You are in a dark forest. You are walking. It has come to an end. You can see a mountain. And you can go left or right. Which way would you like to go? Left, right or do you wanna climb the mountain?")
    print(">Left\n>Right\n>Climb")

    answer = take_command().lower()


    if 'left' in answer:

        print("You come to a river, you can use the bridge or swim across?")
        speak("You come to a river, you can use the bridge or swim across?")
        print(">Walk\n>Swim\n")
        answer = take_command()

        if 'swim' in answer:

            print("You swim across and were eaton by an alligator.")
            speak("You swim across and were eaton by an alligator.")

            print("Do you want to play again?")
            speak("Do you want to play again?")
            play = take_command()

        elif 'bridge' in answer:

            print("The bridge has no capacity to hold you. The bridge broke.")
            speak("The bridge has no capacity to hold you. The bridge broke.")

            print("Do you want to play again?")
            speak("Do you want to play again?")
            play = take_command()

        else:

            print("Not a valid option. you lose!")
            speak("Not a valid option. you lose!")

            print("Do you want to play again?")
            speak("Do you want to play again?")
            play = take_command()


    elif 'right' in answer:
        print("You come to a bridge, it looks wobbly, do you want to go back or cross it?")
        speak("You come to a bridge, it looks wobbly, do you want to go back or cross it?")
        answer = take_command()

        if 'back' in answer:
            print("You go back. You were caught by a Lizard. He took you to a dark place. You can not escape from there. Now you are his slave. The lizard was a human. You have to wait for him to turn into a human.")
            speak("You go back. You were caught by a Lizard. He took you to a dark place. You can not escape from there. Now you are his slave. The lizard was a human. You have to wait for him to turn into a human.")
            
        elif 'cross' in answer:
            print("You cross the bridge and meet a stranger. Do you talk to them?")
            speak("You cross the bridge and meet a stranger. Do you talk to them?")
            answer = take_command()

            if 'yes' in answer:

                print("You talk to the stranger and he give you gold. You win!")
                speak("You talk to the stranger and he give you gold. You win!")

            elif 'no' in answer:
                
                print("You ignore the stranger and they are offended and you lose.")
                speak("You ignore the stranger and they are offended and you lose.")

                print("Do you want to play again?")
                speak("Do you want to play again?")
                play = take_command()

            else:
                
                print("Not a valid option! You Lose.")
                speak("Not a valid option! You Lose.")
                quit()

        else:
            
            print("Invalid Option. You Lose!")
            speak("Invalid Option. You Lose!")
            quit()


    elif 'climb' in answer:

        print("You climb the mountain. You can see two stones to use as a help to finish ur climbing. Which one would you like to choose?\n>Left\n>Right")
        speak("You climb the mountain. You can see two stones to use as a help to finish ur climbing. Which one would you like to choose? Left or Right")
        print(">Left\n>Right\n")
        answer = take_command()

        if 'left' in answer:

            speak("You end up in the lizard's palace. You were eaton by lizard.")
            print("You end up in the lizard's palace. You were eaton by lizard.")

            print("Do you want to play again?")
            speak("Do you want to play again?")
            play = take_command()

        elif 'right' in answer:

            print("You die!")
            speak("You die!")
            
            print("Do you want to play again?")
            speak("Do you want to play again?")
            play = take_command()

        else:
            
            print("Invalid Option. You Lose!")
            speak("Invalid Option. You Lose!")
            quit()

    else:
        
        print("Oops! Invalid Option! You lose!")
        speak("Oops! Invalid Option! You lose!")
        quit()
