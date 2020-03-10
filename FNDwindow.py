# -*- coding: utf-8 -*-
"""
Created on Mon 20 Jan 17:45:40 2020

@author: Nabeel Gm
"""

import pickle
from tkinter import *

def FNwindow():
    gui=Tk()
    gui.title("Fake News Detection")
    gui.configure(background='lightgreen')
    gui.geometry('500x500')
    label_0 = Label(gui, text="Fake News Detection",width=20,font=("bold", 25),bg='lightgreen')
    label_0.place(x=90,y=53)
    label_1 = Label(gui, text="Enter the news you want to verfiy:",width=30,font=("bold", 10),bg='lightgreen')
    label_1.place(x=15,y=128)
    ip=Entry(gui)
    ip.place(x=240,y=130)
    button = Button(gui, text=' Check ', fg='black', bg='cyan', 
                     command=(lambda:detecting_fake_news(ip.get())))
    button.place(x=370,y=128)
    def detecting_fake_news(var):
        
    
        print("processing...")
        print("Entered news is : ",var)
        load_model = pickle.load(open('final_model.sav', 'rb'))
        prediction = load_model.predict([var])
        prob = load_model.predict_proba([var])

        label_2 = Label(gui, text=f"The given statement is {prediction[0]}",width=40,font=("bold", 12),bg='lightgreen')
        label_2.place(x=90,y=153)
        label_3 = Label(gui, text=f"The truth probability score is {prob[0][1]}",width=40,font=("bold", 10),bg='lightgreen')
        label_3.place(x=90,y=180)
        gui.mainloop()

