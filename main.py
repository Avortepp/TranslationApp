import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

def translate_text():
    translator = Translator()
    
    source_language = source_lang_combobox.get()
    target_language = target_lang_combobox.get()
    text = source_text.get("1.0", tk.END).strip()
    
    if not text:
        messagebox.showerror("Input Error", "Please enter some text to translate.")
        return
    
    try:
        translated = translator.translate(text, src=source_language, dest=target_language)
        target_text.delete("1.0", tk.END)
        target_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Creating the main window
root = tk.Tk()
root.title("Text Translator")

# Creating the main container
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

#Field for entering source text
ttk.Label(frame, text="Source Text").grid(row=0, column=0, padx=5, pady=5)
source_text = tk.Text(frame, height=10, width=50)
source_text.grid(row=1, column=0, padx=5, pady=5)

#Drop-down list for selecting the source language
ttk.Label(frame, text="Source Language").grid(row=2, column=0, padx=5, pady=5)
source_lang_combobox = ttk.Combobox(frame, values=['en', 'es', 'fr', 'de', 'ru'])
source_lang_combobox.set('en')  #Set English as the default language
source_lang_combobox.grid(row=3, column=0, padx=5, pady=5)

# Drop-down list for selecting the target language
ttk.Label(frame, text="Target Language").grid(row=4, column=0, padx=5, pady=5)
target_lang_combobox = ttk.Combobox(frame, values=['en', 'es', 'fr', 'de', 'ru'])
target_lang_combobox.set('ru')  # Set Russian as the default language
target_lang_combobox.grid(row=5, column=0, padx=5, pady=5)

# Button for text translation
translate_button = ttk.Button(frame, text="Translate", command=translate_text)
translate_button.grid(row=6, column=0, padx=5, pady=5)

# Field for displaying translated text
ttk.Label(frame, text="Translated Text").grid(row=7, column=0, padx=5, pady=5)
target_text = tk.Text(frame, height=10, width=50)
target_text.grid(row=8, column=0, padx=5, pady=5)
 
 
# Launching the application
root.mainloop()