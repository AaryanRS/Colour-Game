import tkinter
import random
from tkinter import *
from tkinter import font

coloursList = ["red" , "pink" , "blue" , "green" , "black" , "blue" , "brown" , "orange" , "white" , "purple"]
score = 0

timeleft = 30
def startGame(event) :
    if timeleft == 30:
        countdown()
    nextcolour()

def nextcolour():
    global score 
    global timeLeft

    if timeleft>0:
        colourEntry.focus_set()
        if colourEntry.get().lower()==coloursList[1].lower():
            score += 1
    colourEntry.delete(0,tkinter.END)
    random.shuffle(coloursList)
    colourLabel.config(fg =str(coloursList[1]),text=str(coloursList[0]))
    scoreLabel.config(text="score:  "+str(score))

def countdown():
    global timeleft
    if timeleft > 0 :
        timeleft-=1
        timeLabel.config(text="Time Left:  "+str(timeleft))
        timeLabel.after(1000,countdown)

#Creating the GUI window-
root=tkinter.Tk()
root.title("Colour Game")
root.geometry('400x200')

instructions = Label (root,text="Type the colour of a word, but not the word text",font="times 14 bold")
instructions.pack()

scoreLabel = Label (root,text="Press Enter to start",font= "times 14 bold")
scoreLabel.pack()

timeLabel = Label (root,text="Time Left: ",font= "times 14 bold")
timeLabel.pack()

colourLabel = Label (root,font="times 14 bold")
colourLabel.pack()

colourEntry=Entry(root)
colourEntry.pack()

#When the enter key is pressed 
root.bind("<Return>",startGame)
colourEntry.focus_set()

root.mainloop()

