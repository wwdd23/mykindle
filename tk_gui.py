#!/usr/bin/env python
#-*- coding:utf-8 -*-
############################
#File Name: tk_gui.py
#Author: wudi
#Mail: programmerwudi@gmail.com
#Created Time: 2015-06-18 15:50:22
############################

from Tkinter import *

root=Tk(className='Change name')

def on_click():
    label['text'] = text.get()

#var = StringVar()
#label= Label(root, textvariable=var )
label= Label(root)
label['text'] = 'text change'
#var.set("text change")
label.pack()

text = StringVar()
text.set('What?')

entry=Entry(root)
entry['textvariable'] = text
entry.pack()


#button=Button(root, text='change it',command=on_click)
button = Button(root)
button['text'] = 'change it'
button['command'] = on_click

button.pack()
bt1= Button(root,text='exit',command=root.quit)
bt1.pack()


root.mainloop()
