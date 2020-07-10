# Matrix Loves You : packages/convert.py

# Imports
from mLib import identify, var
from tkinter import messagebox as c_messagebox, simpledialog as c_inputbox, Tk
from fractions import Fraction as fnd
import math, os, sys

# Functions
def data(t_matrixes):
    t_new = list(())
    for t_keys in t_matrixes.keys():
        t_matrix = dict(())
        t_matrix['name'] = t_keys
        t_value = t_matrixes.get(t_keys)
        t_matrix['row'] = len(t_value)
        t_matrix['col'] = len(t_value[0])
        t_matrix['count'] = len(t_value)*len(t_value[0])
        t_matrix['value'] = mType(t_value)
        t_matrix['call'] = name(t_keys, t_matrix.get('value'))
        t_matrix['type'] = identify.matrix(t_matrix)
        t_new.append(t_matrix)
    return t_new

def mType(t_matrix):
    new_matrix = list(())
    for each_row in t_matrix:
        new_row = list(())
        for each_col in each_row:
            t_value = number(each_col)
            new_row.append(t_value)
        new_matrix.append(new_row)
    return new_matrix

def number(n_input):
    if len(n_input) > 23:
        print("Error : String too long")
        c_messagebox.showerror("Error", "Program needs to restart")
        os.system(var.restartPath, var.restartArgs[0])
        sys.exit(0)
    t_text = ""
    find_state = True
    for each_index in range(len(n_input)):
        each_char = n_input[each_index]
        if each_char in var.Integer or each_char == var.Matsymbol[1]:
            if find_state:
                find_first = each_index
                find_state = False
            t_text += each_char
            find_last = each_index
        elif find_state == False and each_char not in var.Integer and each_char != var.Matsymbol[1]:
            break
    t_temp = float(t_text)
    if t_temp.is_integer():
        t_temp = int(t_temp)
    if len(n_input) > 1:
        if (find_first - 1) >= 0 and n_input[find_first - 1] == var.Matsymbol[0]:
            t_temp *= -1
            find_first -= 1
        if (find_first - 1) >= 0 and (find_last + 1) <= (len(n_input) - 1) and n_input[find_first - 1] == var.Matsymbol[2] and n_input[find_last + 1] == var.Matsymbol[2]:
            t_temp = abs(t_temp)
            find_first -= 1
            find_last += 1
        if (find_last + 1) <= (len(n_input) - 1) and n_input[find_last + 1] == var.Matsymbol[3]:
            e_text = ""
            for each_index in range(find_last + 2, len(n_input)):
                each_char = n_input[each_index]
                if each_char in var.Integer or each_char == var.Matsymbol[1]:
                    e_text += each_char
                    find_state = True
                else:
                    break
            t_temp **= float(e_text)
            find_last += 1 + len(e_text)
        if (find_last + 1) <= (len(n_input) - 1) and n_input[find_last + 1] == var.Matsymbol[4]:
            if t_temp < 0:
                print("Error : Unable to factorize negative number")
                #f_input = input("Please enter the replacement for "+ t_name +"("+ (t_matrix.index(each_row) + 1) +", "+ (each_row.index(each_col) + 1) +") : ")
                input()
                c_messagebox.showerror("Error", "Program needs to restart")
                os.system(var.restartPath +" "+ var.restartArgs[0])
                sys.exit(0)
            elif t_temp == 0:
                pass
            elif t_temp > 0 and type(t_temp) == float:
                print("Error : Cannot factorize decimals")
                #f_input = input("Please enter the replacement for "+ t_name +"("+ (t_matrix.index(each_row) + 1) +", "+ (each_row.index(each_col) + 1) +") : ")
                input()
                c_messagebox.showerror("Error", "Program needs to restart")
                os.system(var.restartPath +" "+ var.restartArgs[0])
                sys.exit(0)
            elif t_temp > 0 and type(t_temp) == int:
                t_temp = math.factorial(t_temp)
                find_last += 1
        if (find_first - 1) >= 0 and n_input[find_first - 1] == var.Matsymbol[0]:
            t_temp *= -1
            find_first -= 1
    if type(t_temp) == float and t_temp.is_integer() or type(t_temp) == int:
        t_value = [int(t_temp), 1]
    else:
        t_value = str(fnd(float(t_temp)).limit_denominator()).split("/")
        t_value = [int(t_value[0]), int(t_value[1])]
    return t_value

def name(n_name, n_matrix):
    n_long = list(())
    for n_each in range(len(n_matrix[0])):
        n_long.append(0)
    for n_row in n_matrix:
        for n_index in range(len(n_row)):
            n_col = n_row[n_index]
            if n_row[n_index][1] == 1:
                n_col = str(n_row[n_index][0])
            else:
                n_col = str(n_row[n_index][0]) +"/"+ str(n_row[n_index][1])
            if len(n_col) > n_long[n_index]:
                n_long[n_index] = len(str(n_col)) + (7 - len(str(n_col)) % 7)
    p_string = n_name +" :\t"
    p_long = math.ceil(len(p_string[:-1]) / 7)
    for each_index in range(len(n_matrix)):
        each_row = n_matrix[each_index]
        if len(n_matrix) == 1:
            p_string += "[ "
        elif len(n_matrix) > 1 and each_index == 0:
            p_string += u"\u2308"+" "
        elif len(n_matrix) > 1 and each_index == len(n_matrix) - 1:
            p_string += "\t"* p_long +u"\u230A"+" "
        else:
            p_string += "\t"* p_long +u"\u007C"+" "
        for each_col_index in range(len(each_row)):
            each_col = each_row[each_col_index]
            if each_col[1] == 1:
                each_col = str(each_col[0])
            else:
                each_col = str(each_col[0]) +"/"+ str(each_col[1])
            n_tab = math.ceil((n_long[each_col_index] - len(each_col)) / 7)
            p_string += str(each_col) +"\t"* n_tab
        if len(n_matrix) == 1:
            p_string += "]"
        elif len(n_matrix) > 1 and each_index == 0:
            p_string += u"\u2309"+"\n"
        elif len(n_matrix) > 1 and each_index == len(n_matrix) - 1:
            p_string += u"\u230B"
        else:
            p_string += u"\u007C"+"\n"
    del n_each
    return p_string