#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: entry.py
#Author: wudi
#Mail: programmerwudi@gmail.com
#Created Time: 2015-02-14 16:40:18
############################

from Tkinter import *

root = Tk()

e = Entry(root)

e.pack()

e.focus_set()

def callback():
        print e.get()

b = Button(root, text='get', width = 10,command=callback)
b.pack()

mainloop()
