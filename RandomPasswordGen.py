import random
import string
import tkinter as tk
import atexit

window = tk.Tk()
window.geometry("500x600")
window.config(bg="#404040")

title = tk.Label(text="Random Password Generator")
title.pack(pady=(10,0))

title.config(font=("Arial", 20))
text1 = tk.Label(text="Amount of Characters")
text1.pack(pady=(30, 0))

entry = tk.Entry(text = "How many Num?")
entry.pack()

password = []


def gen():
    password.clear()
    length = int(entry.get())


    possibleChars = string.ascii_letters + string.digits + string.punctuation



    for x in range(length):
        password.append(random.choice(possibleChars))


generate = tk.Button(text="Generate", command = gen)
generate.pack()




list = tk.Listbox(width=80, height=20, selectmode=tk.EXTENDED)
list.pack(pady=(30, 0))

amountItems = 0

def deleteItem():
    list.delete(tk.ANCHOR)

delete = tk.Button(text="Delete", command=deleteItem)
delete.pack()

text2 = tk.Label(text="What the password is for")
text2.pack()

nameofPass = tk.Entry()
nameofPass.pack()

def addItem():
    if(not password):
        {
            password.append("Click Gen")
        }
    list.insert(0, nameofPass.get() + " = " + ''.join(password))



addButton = tk.Button(text="Add Password", command=addItem)
addButton.pack()

def listboxCopy(event):
    window.clipboard_clear()
    selected = list.get(tk.ANCHOR)
    window.clipboard_append(selected)

list.bind('<Double-Button-1>', listboxCopy)


title.config(bg="#404040", fg="white")
text1.config(bg="#404040", fg="white")
text2.config(bg="#404040", fg="white")
list.config(bg="#505050", fg="white")
nameofPass.config(bg="#606060", fg="white")
entry.config(bg="#606060", fg="white")
generate.config(bg="gray", fg='white')
delete.config(bg="gray", fg='white')
addButton.config(bg="gray", fg='white')






window.mainloop()
