# -*- coding: utf-8 -*-

from main import Main 


def name():
    return "angulo reto"
def description():
    return "teste"
def version():
    return "Version 0.1"

def classFactory(iface):
    return Main(iface)

def qgisMinimumVersion():
    return "2.0"
def author():
    return "Felipe Diniz e jossan costa"
def email():
    return "me@hotmail.com"
def icon():
    return "icon.png"

