# Matrix Loves You : push/execute.py

# Imports
from mLib import var
from tkinter import messagebox as w_messagebox, simpledialog as w_inputbox, Tk
from bs4 import BeautifulSoup
from inscriptis import get_text
import urllib.request, sys, webbrowser

# Functions
def welcome(w_code):
    Tk().withdraw()
    if w_code == -1:
        w_messagebox.showwarning("Warning", "Section under construction\nPlease check for further update")
    elif w_code == 0:
        w_messagebox.showinfo("Matrix Loves You", "Welcome\nThis program will help you all with matrixes")
        print("TheMatrix : All about matrix")
        print("By : Tecillium (UFDT) - TianTcl.net")
        print("Version : "+ var.appVersion +" | "+ var.appVername)
        print("Modified : "+ var.appModified)
    elif w_code == 1:
        w_messagebox.showinfo("Matrix Loves You : Cramer", "Welcome to \"Cramer\" mode\nPlease input your expressions for the program will find out the variables value for you")

def update_check():
    try:
        last_version = str(BeautifulSoup(urllib.request.urlopen("https://TianTcl.net/ref/TheMatrix/app/version.tclt"),features="lxml").findAll(text=True))[2:-4]
        my_version = var.appVersion
        if my_version == last_version:
            return False
        elif my_version != last_version:
            return w_messagebox.askyesnocancel("Important!", "Update is available\nCurrent version\t: "+my_version+"\nLastest version\t: "+last_version+"\nDo you want to update your app?")
    except:
        return False

def update_action(ua_permission):
    if ua_permission:
        webbrowser.open(str(BeautifulSoup(urllib.request.urlopen("https://TianTcl.net/ref/TheMatrix/app/name.tclt"),features="lxml").findAll(text=True))[2:-4])
        sys.exit(0)
    elif ua_permission == None:
        sys.exit(0)