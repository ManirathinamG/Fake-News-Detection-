from tkinter import *
import pickle
import FNDwindow
from warnings import simplefilter
simplefilter(action='ignore',category=UserWarning)


def CheckLogin():
    
    # This takes the entire document we put the info into and puts it into the data variable
    uname = "Nabeel" # Data[0], 0 is the first line, 1 is the second and so on.
    pword = "1234" # Using .rstrip() will remove the \n (new line) word from before when we input it
 
    if nameEL.get() == uname and pwordEL.get() == pword:
        FNDwindow.FNwindow()
    
    else:
        gui = Tk()
        gui.configure(background="light green")
        gui.geometry('250x100')
        gui.title('Error')
        label_0= Label(gui, text='\n[!] Invalid Login',fg='red',bg='lightgreen')
        label_0.pack()
        gui.mainloop()
 

def detecting_fake_news(var):
    
    print("processing...")
    print("Entered news is : ",var)
#retrieving the best model for prediction call
    load_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    label_2 = Label(gui, text=f"The given statement is {prediction[0]}",width=40,font=("bold", 12),bg='lightgreen')
    label_2.place(x=90,y=153)
    label_3 = Label(gui, text=f"The truth probability score is {prob[0][1]}",width=40,font=("bold", 10),bg='lightgreen')
    label_3.place(x=90,y=180)
    gui.mainloop()


global nameEL
global pwordEL # More globals :D
global rootA

 
rootA = Tk() # This now makes a new window.
rootA.title('Login')# This makes the window title 'login'
rootA.geometry('250x150')
intruction = Label(rootA, text='Please Login\n',bg='lightgreen') # More labels to tell us what they do
intruction.grid(sticky=E) # Blahdy Blah
rootA.configure(background='lightgreen')
nameL = Label(rootA, text='Username: ',bg='lightgreen') # More labels
pwordL = Label(rootA, text='Password: ',bg='lightgreen') # ^
nameL.grid(row=1, sticky=W)
pwordL.grid(row=2, sticky=W)
 
nameEL = Entry(rootA) # The entry input
pwordEL = Entry(rootA, show='*')
nameEL.grid(row=1, column=1)
pwordEL.grid(row=2, column=1)
 
loginB = Button(rootA, text='Login', command=CheckLogin,bg='orange') # This makes the login button, which will go to the CheckLogin def.
loginB.grid(columnspan=2, sticky=W)
 
rootA.mainloop()
 
