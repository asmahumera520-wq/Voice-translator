from tkinter import *
from deep_translator import GoogleTranslator
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def translate_text():
    input_text = text_box.get("1.0", END).strip()
    target_lang = lang_var.get()
    if input_text:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(input_text)
        output_box.config(state=NORMAL)
        output_box.delete("1.0", END)
        output_box.insert(END, translated)
        output_box.config(state=DISABLED)
        engine.say(translated)
        engine.runAndWait()
    else:
        output_box.config(state=NORMAL)
        output_box.delete("1.0", END)
        output_box.insert(END, "Please enter text or use voice input.")
        output_box.config(state=DISABLED)

def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        output_box.config(state=NORMAL)
        output_box.delete("1.0", END)
        output_box.insert(END, "Listening...")
        output_box.config(state=DISABLED)
        r.adjust_for_ambient_noise(source, duration=1)  # calibrate to background noise
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            text_box.delete("1.0", END)
            text_box.insert(END, text)
            translate_text()
        except:
            output_box.config(state=NORMAL)
            output_box.delete("1.0", END)
            output_box.insert(END, "Sorry, could not understand your voice.")
            output_box.config(state=DISABLED)

root = Tk()
root.title("Voice & Text Translator Chatbot")
root.geometry("500x450")

Label(root, text="Enter text or speak:", font=("Arial", 12)).pack(pady=5)
text_box = Text(root, height=5, width=50)
text_box.pack(pady=5)

Label(root, text="Select target language:", font=("Arial", 12)).pack(pady=5)
lang_var = StringVar()
lang_var.set("te")

languages = {"Telugu": "te", "Hindi": "hi", "Tamil": "ta", "Kannada": "kn"}
lang_menu = OptionMenu(root, lang_var, *languages.values())
lang_menu.pack(pady=5)

Button(root, text="Translate Text", command=translate_text, bg="lightblue", font=("Arial", 12)).pack(pady=5)
Button(root, text="Voice Input", command=voice_input, bg="lightgreen", font=("Arial", 12)).pack(pady=5)

Label(root, text="Translated text:", font=("Arial", 12)).pack(pady=5)
output_box = Text(root, height=5, width=50, state=DISABLED)
output_box.pack(pady=5)

root.mainloop()