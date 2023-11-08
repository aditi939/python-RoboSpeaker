import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker Created by Aditi: ")
    while True:
        x = input("Enter what you want to speak:  ")
        if x == "q":
            break
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Say the user's input
        engine.say(x)

        # Wait for the speech to finish
        engine.runAndWait()
