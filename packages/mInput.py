# Matrix Loves You : packages/mInput.py

# Imports
from mLib import var
from tkinter import messagebox as t_messagebox, simpledialog as t_inputbox, Tk
import os, sys

# Initialize
m_store = {}
Tk().withdraw()

# Functions
def run():
    print("\nPlease input at least 1 matrix\t\t\t(type \"uc\" to enter Cramer's mode)")
    while True:
        r_name = var_name()
        if r_name == "end-input":
            break
        elif r_name == "use-cramer":
            os.system(var.restartPath +" "+ var.restartArgs[1])
            sys.exit(0)
        r_matrix = matrix(r_name)
        if r_matrix != "empty":
            m_store[r_name] = r_matrix
    return m_store

def var_name():
    while True:
        v_name = input("Variable name : ")
        if v_name == "" and len(m_store) != 0:
            return "end-input"
            break
        elif v_name.lower() == "uc":
            return "use-cramer"
        elif v_name not in m_store.keys():
            if len(v_name) == 1:
                if v_name in var.Lowercase or v_name in var.Uppercase:
                    return v_name.upper()
                    break
                else:
                    print("Info : A variable name must be an alphabet")
            else:
                print("Info : A variable name can only be 1 character long")
        else:
            print("Info : This variable name has been used")

def matrix(m_name):
    m_new = list(())
    m_round = "1234567890"
    for m_line in m_round:
        m_row = list(())
        if m_line == "1":
            m_input = input(m_name+" =\t")
        else:
            m_input = input("\t")
        m_each_state = set(())
        for m_each_char in m_input:
            if m_each_char not in var.Input:
                m_each_state.add(False)
        if False not in m_each_state:
            if len(m_input) > 1 and m_input[-1] in var.Delimiter:
                m_input = m_input[:-1]
            if len(m_input) > 1 and m_input[0] in var.Delimiter:
                m_input = m_input[1:]
            if m_input == "" and m_line != "1":
                break
            m_col = 1
            if m_input != "":
                for m_each in var.Delimiter:
                    if m_each in m_input:
                        m_delimeter = m_each
                        m_col = 0
                        break
            if len(m_new) == 0 and m_input == "":
                print("Error : Please enter a value")
                m_round += "."
            if m_line == m_round[-2]:
                t_messagebox.showwarning("Warning", "The next row is your last!")
            if m_col == 1 and len(m_new) == 0:
                m_pass = set(())
                for m_char in m_input:
                    if m_char in var.Common:
                        m_pass.add(True)
                if False not in m_pass:
                    m_row.append(m_input)
                else:
                    print("Error : Invalid character")
                    m_round += "."
            elif m_col == 1 and len(m_new) != 0:
                m_state = True
                for m_each in var.Delimiter:
                    if m_each in m_input:
                        print("Error : You can't more column than the first row's")
                        m_round += "."
                        m_state = False
                    break
                if m_state:
                    m_pass = set(())
                    for m_char in m_input:
                        if m_char in var.Common:
                            m_pass.add(True)
                    if False not in m_pass:
                        m_row.append(m_input)
                    else:
                        print("Error : Invalid character")
                        m_round += "."
            elif m_col == 0:
                m_col = len(m_input.split(m_delimeter))
            if m_col > 1:
                m_col_new = len(m_input.split(m_delimeter))
                if m_col > 1 and m_col <= 10:
                    if m_col_new == m_col:
                        for m_member in m_input.split(m_delimeter):
                            m_ps = set(())
                            for m_char in m_member:
                                m_pass = set(())
                                if m_char in var.Common:
                                    m_pass.add(True)
                            if False not in m_pass:
                                m_ps.add(True)
                            else:
                                m_ps.add(False)
                        if True in m_ps:
                            m_row = m_input.split(m_delimeter)
                        else:
                            print("Error : Invalid character")
                            m_round += "."
                    else:
                        print("Error : Each row must have the same amount of columns")
                        m_round += "."
                else:
                    print("Error : You can't have more than 10 column")
                    m_round += "."
                    del m_col
            if len(m_row) >= 1:
                m_new.append(m_row)
        else:
            print("Error : Invalid character")
            m_round += "."
    if len(m_new) >= 1:
        return m_new
    else:
        return "empty"

def once(o_var):
    while True:
        r_name = var_name()
        if r_name not in o_var and r_name != "end-input":
            break
        else:
            print("Info : This variable name has been used")
    while True:
        r_matrix = matrix(r_name)
        if r_matrix != "empty":
            break
    return {r_name : r_matrix}