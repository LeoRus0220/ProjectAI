import speech_recognition as sr

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

if __name__ == "__main__":
  command = listen_for_command()
  # You'll add more logic here to handle different commands