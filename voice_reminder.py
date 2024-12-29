import speech_recognition as sr
import datetime

print("Script started")  # Add this line

def listen_for_command():
    """Listens for a voice command and returns the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1  # Adjust this to change pause sensitivity
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)  # Uses Google Speech Recognition
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

def set_reminder(command):
    """
    Extracts reminder details and sets a reminder.
    For now, just prints a message to the console.
    """
    now = datetime.datetime.now()
    try:
        # Split the command by spaces
        words = command.lower().split()  
        # Find the index of "in"
        in_index = words.index("in")  
        # Find the index of "minutes" or "minute"
        try:
            minutes_index = words.index("minutes")  
        except ValueError:
            minutes_index = words.index("minute")
        # Extract the number between "in" and "minutes"/"minute"
        minutes = int(words[in_index + 1])  
        reminder_time = now + datetime.timedelta(minutes=minutes)
        print(f"Reminder set for {reminder_time}")
    except (ValueError, IndexError):
        print("Sorry, I couldn't understand the time.")

if __name__ == "__main__":
    print("Starting script...")  # Add this line
    command = listen_for_command()
    print("Command received:", command)  # Add this line
    if "reminder" in command.lower():
        set_reminder(command)