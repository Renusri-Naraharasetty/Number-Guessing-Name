import tkinter as tk
import random

number=random.randint(1,100)
attempt=0

def check():
    global attempt
    guess=entry.get()
    
    if not guess.isdigit():
        result.config(text="Please enter a valid number !!")
        return
    
    guess=int(guess)
    attempt+=1
    
    if guess<number:
        result.config(text="Too Low!")
    elif guess>number:
        result.config(text="Too High!")
    else:
        result.config(text=f"Yayy!! You got it right :) \nYou got it in {attempt} tries.")

root=tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x250")
# root.resizable(False, False)

title_label=tk.Label(root,text="Guess the number between 1 to 100",font=("Arial",12))
title_label.pack(pady=10)

entry=tk.Entry(root, font=("Arial",12), justify='center')
entry.pack(pady=5)

guess_button=tk.Button(root, text="Guess", font=("Arial",11), command=check)
guess_button.pack(pady=5)

result=tk.Label(root, text="", font=("Arial", 11))
result.pack(pady=10)

root.mainloop()