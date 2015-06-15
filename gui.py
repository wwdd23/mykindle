#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: gui.py
#Author: wudi
#Mail: programmerwudi@gmail.com
#Created Time: 2015-02-06 16:42:26
############################



import Tkinter 


from tkMessageBox import *

top = Tkinter.Tk()

def cancel_click():
        showinfo('温馨提示','您点击【取消】操作')
        close.Tk()
def save_click():
        showinfo('温馨提示','您点击【保存】操作')



btn_Cancel=Tkinter.Button(top,text='取消')
btn_Cancel.pack(side=Tkinter.RIGHT)


btn_Save=Tkinter.Button(top,
        anchor=Tkinter.E,       #指定对齐方式
        text='保存',           #指定按钮上的文本
        width=40,               #指定按钮宽度，相当于40个字符
        height=5,                #指定按钮高度，相当于5个字符
        command=save_click       #绑定事件
        )
btn_Save.pack()

top.mainloop()
