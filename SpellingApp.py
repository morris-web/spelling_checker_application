import tkinter
from tkinter import *
from textblob import TextBlob

root = tkinter.Tk()
root.title("Spelling Checker")
root.geometry("700x400")  
root.config(background="#dae6f6")

def check_spelling():
    word = enter_text.get()
    if word.strip() == "":
        spell.config(text="Please enter some text.")
        return
    try:
        a = TextBlob(word)
        corrected_text = str(a.correct())
        spell.config(text=f"Correct text is: {corrected_text}")
    except Exception as e:
        spell.config(text="Error in processing text.")

heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50,0))

enter_text = Entry(root, justify="center", width=30, font=("Poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = Button(root, text="Check", font=("Arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
button.pack()

spell = Label(root, font=("Poppins", 20), bg="#dae6f6", fg="#364971")
spell.place(x=100, y=250)

root.mainloop()
