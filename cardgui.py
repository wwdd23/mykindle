#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: cardgui.py
#Author: wudi
#Mail: programmerwudi@gmail.com
#Created Time: 2015-02-08 11:49:51
############################

from PythonCard import model

class MainWindow(model.Background):
    pass

app = model.Apllication(MainWindow)
app.MainLoop()
