#Import the required Libraries
from tkinter import *
from tkinter import ttk
import openai
openai.api_key = "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"
openai.api_endpoint = "https://api.openai.com/v1/completions"

def showChar(n, txt):
    n += 1
    label.config(text = txt[:n])
    if n < len(txt):
        win.after(10, lambda: showChar(n, txt))


def userinput_to_AI(e):
    n = 0
    global entry
    string= entry.get()
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=string,
    max_tokens=4800,
    n=1,
    temperature=0.5,)
    answer=response["choices"][0]["text"]
    showChar(n, answer)
    #label.configure(text=answer)
    #var.set(answer)




#Create an instance of Tkinter frame
win= Tk()
win.title("Welcome to Your AI Assistant")
win.resizable(width=True , height=True)
#Set the geometry of Tkinter frame
win.geometry("750x300")


def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 12"), width=100, bg="white", fg="black", wraplength=500, justify=LEFT)
label.pack()

Label(win, text= "Press Enter on the Keyboard after User Input", font= ('Helvetica', 14)).pack(pady=20)

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

ent = Entry(win, state='readonly', readonlybackground='white', fg='black', width=100, bd=0, justify=LEFT)
var = StringVar()

ent.config(textvariable=var, relief='flat')
ent.pack()
#Create a Button to validate Entry Widget
#ttk.Button(win, text= "Click or Press Enter",width= 20, command= userinput_to_AI).pack(pady=20)
win.bind('<Return>', userinput_to_AI)


win.mainloop()




