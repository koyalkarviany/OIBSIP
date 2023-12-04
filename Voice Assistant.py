import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyautogui

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()



def respond(response_text):
    print(response_text)

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    global tasks 

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source) # ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you repeat?")
            return ""
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")
            return ""



# Main loop
speak("Hello! I'm your voice assistant. How can I help you")


# Function to execute commands
def execute_command(command):

    if "what is your name" in command:
        speak("my name is vinay.I am your voice assistant.")
    
    elif "hello" in command:
       speak("Hello! How can I assist you?")
  
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")
        speak("opening youtube.")

    elif "google" in command:
        webbrowser.open("https://www.google.com/")
        speak("opening google.")
    
    elif "open chrome" in command:
        webbrowser.open("https://www.google.com/")
        speak("opening chrome.")
    
    elif "add a task" in command:
        listeningToTask = True
        speak,respond("Sure, what is the task?")

    elif "list tasks" in command:
        speak("Sure. Your tasks are:")
        for task in tasks:
         speak(task)

    elif "take a screenshot" in command:
        pyautogui.screenshot("screenshot.png")
        speak("I took a screenshot for you.")

    elif "goodbye" in command:
        speak("Goodbye! Have a great day!")
        exit()

    elif command in command:
        webbrowser.open (command)     

    else:
        speak("I'm not sure how to handle that command.")

while True:
    user_command = recognize_speech()

    if user_command:
        execute_command(user_command)
        respond(user_command)
