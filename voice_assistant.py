"""
Simple AI Voice Assistant
--------------------------
Greets the user, then listens for voice commands like "open notepad".

Install dependencies first:
    pip install pyttsx3 SpeechRecognition pyaudio

Note: On Windows, pyaudio installs easily via pip.
On Mac/Linux, you may need portaudio first:
    Mac:   brew install portaudio
    Linux: sudo apt-get install portaudio19-dev
"""

import pyttsx3
import speech_recognition as sr
import subprocess
import sys
import os
import datetime


# ---------- SETUP ----------
engine = pyttsx3.init()

# Optional: adjust voice properties
engine.setProperty('rate', 170)     # speaking speed
engine.setProperty('volume', 1.0)   # volume 0.0 to 1.0

# Try to pick a female voice if available (optional)
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break


def speak(text):
    """Convert text to speech."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to microphone and convert speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return ""

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable right now.")
        return ""


def greet():
    """Greet based on time of day."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    speak(f"{greeting}, Meghana. How can I help you today?")


def open_application(app_name):
    """Open an application based on the platform."""
    app_name = app_name.strip().lower()

    apps = {
        "windows": {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
        },
        "darwin": {  # macOS
            "notepad": "TextEdit",
            "calculator": "Calculator",
        },
        "linux": {
            "notepad": "gedit",
            "calculator": "gnome-calculator",
        },
    }

    platform = sys.platform
    if platform.startswith("win"):
        os_key = "windows"
    elif platform.startswith("darwin"):
        os_key = "darwin"
    else:
        os_key = "linux"

    target = apps.get(os_key, {}).get(app_name)

    if not target:
        speak(f"I don't know how to open {app_name} on this system.")
        return

    try:
        if os_key == "windows":
            os.startfile(target) if app_name != "notepad" else subprocess.Popen(target)
        elif os_key == "darwin":
            subprocess.Popen(["open", "-a", target])
        else:
            subprocess.Popen([target])
        speak(f"Opening {app_name}")
    except Exception as e:
        speak(f"I couldn't open {app_name}. Error: {e}")


def handle_command(command):
    """Route recognized command text to an action."""
    if "open notepad" in command:
        open_application("notepad")
    elif "open calculator" in command:
        open_application("calculator")
    elif "open paint" in command:
        open_application("paint")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    elif "exit" in command or "stop" in command or "quit" in command:
        speak("Goodbye, Meghana. Shutting down.")
        return False
    elif command == "":
        pass  # nothing recognized, just loop again
    else:
        speak("I heard you, but I don't have a command set up for that yet.")
    return True


def main():
    speak("Hi Meghana")
    greet()

    running = True
    while running:
        command = listen()
        if command:
            running = handle_command(command)


if __name__ == "__main__":
    main()