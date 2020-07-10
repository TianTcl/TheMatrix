# Matrix Loves You : packages/mPrint.py

# Imports
from mLib import find, get, operate, var
from packages import convert, mInput
import os, sys

# Functions
def console(c_store):
    c_var = get.allvar(c_store)
    print("\n~List of commands~\n"+ var.commandList)
    while True:
        while True:
            c_input = input("\nCommand : ")
            if c_input != "":
                break
        c_list = command(c_input, c_var)
        if c_list == None:
            print("Error : Invalid command")
        elif type(c_list) == str:
            sysadmin(c_list, [c_store, c_var])
        elif len(c_list) == 2:
            case(c_list[0], get.matrix(c_store, c_list[1]))
        elif len(c_list) == 3:
            case(c_list[0], [get.matrix(c_store, c_list[1]), c_list[2], c_store])
        elif len(c_list) == 4:
            case([c_list[0], c_list[2], c_list[3]], get.matrix(c_store, c_list[1]))

def command(c_string, c_var):
    c_return = None
    if c_string in var.commandCode:
        c_return = c_string
    elif len(c_string) == 1:
        c_return = "NoMatrix"
        if c_string.upper() in c_var:
            c_return = ["print", c_string]
    elif len(c_string) == 2 and c_string[1] == "'":
        c_return = "NoMatrix"
        if c_string[0].upper() in c_var:
            c_return = ["transpose", c_string[0]]
    elif "(" in c_string and ")" in c_string:
        c_command = c_string[:c_string.index("(")]
        if c_command in var.commandDeprecated:
            c_return = "NoSupport"
        elif c_command in var.commandLine:
            c_return = "NoMatrix"
            if c_string[len(c_string) - 2].upper() in c_var:
                c_return = [c_string[0:len(c_string) - 3], c_string[len(c_string) - 2]]
        elif c_command in var.commandArgs or c_command in var.commandCalc:
            c_celimeter = ""
            c_arg = c_string[c_string.index("(") + 1:c_string.index(")")]
            for c_each_celimeter in var.Celimeter:
                if c_each_celimeter in c_arg:
                    c_celimeter = c_each_celimeter
                    break
            c_args = c_arg.split(c_celimeter)
            if c_command in var.commandArgs and len(c_args) == 3:
                c_return = "NoMatrix"
                if c_args[0].upper() in c_var:
                    c_ca_state = set(())
                    for c_each_ca_index in [1, 2]:
                        c_each_ca = c_args[c_each_ca_index]
                        c_each_ca_state = set(())
                        for c_each_ca_char in c_each_ca:
                            if c_each_ca_char not in var.Index:
                                c_each_ca_state.add(False)
                        if False not in c_each_ca_state:
                            c_args[c_each_ca_index] = int(c_each_ca)
                        elif False in c_each_ca_state:
                            c_ca_state.add(False)
                    if False not in c_ca_state:
                        c_args.insert(0, c_string[:c_string.index("(")])
                        c_return = c_args
                    elif False in c_ca_state:
                        print("Error : Please check your arguments")
                        c_return = "TakeNoAction"
            elif c_command in var.commandCalc and len(c_args) == 2:
                c_return = "NoMatrix"
                if c_command in var.commandCalc[:4] and c_args[0].upper() in c_var and c_args[1].upper() in c_var:
                    c_args.insert(0, c_string[:c_string.index("(")])
                    c_return = c_args
                elif c_command in var.commandCalc[3:] and c_args[0].upper() in c_var:
                    c_args[1] = convert.number(c_args[1])
                    c_args.insert(0, c_string[:c_string.index("(")])
                    c_return = c_args
                else:
                    print("Error : Please check your arguments")
                    c_return = "TakeNoAction"
            else:
                print("Error : Please check your syntax")
    return c_return

def sysadmin(sa_cmd, sa_attr = None):
    if sa_cmd == "new":
        sa_attr[0].append(convert.data(mInput.once(sa_attr[1]))[0])
        sa_attr[1].append(sa_attr[0][len(sa_attr[0]) - 1].get('name'))
    elif sa_cmd == "help":
        print("\n~List of commands~\n"+ var.commandList +"\n")
    elif sa_cmd == "usage":
        print("\n~Command usage & examples~\n"+ var.commandUsage +"\n")
    elif sa_cmd == "restart" or sa_cmd == "reset":
        os.system(var.restartPath +" "+ var.restartArgs[0])
        sys.exit(0)
    elif sa_cmd == "stop" or sa_cmd == "exit" or sa_cmd == "quit":
        sys.exit(0)
    elif sa_cmd == "TakeNoAction":
        pass
    elif sa_cmd == "NoMatrix":
        print("Info : The requested matrix doesn't exist.")
    elif sa_cmd == "NoSupport":
        print("Info : This command is no longer available")

def case(s_cmd, s_matrix):
    if s_cmd == "print":
        get.value(s_matrix)
    elif s_cmd == "det":
        find.determinant(s_matrix)
    # elif s_cmd == "dim":
    #     get.dimension(s_matrix)
    elif s_cmd == "transpose":
        find.transpose(s_matrix)
    # elif s_cmd == "count":
    #     get.amount(s_matrix)
    # elif s_cmd == "type":
    #     get.category(s_matrix)
    elif s_cmd == "inverse":
        find.inverse(s_matrix)
    elif s_cmd == "prop":
        get.property(s_matrix)
    elif s_cmd[0] == "member":
        get.member(s_matrix, s_cmd[1], s_cmd[2])
    elif s_cmd[0] == "minor":
        find.minor(s_matrix, s_cmd[1], s_cmd[2])
    elif s_cmd[0] == "cofactor":
        find.cofactor(s_matrix, s_cmd[1], s_cmd[2])
    elif s_cmd == "add":
        operate.add(s_matrix[0], get.matrix(s_matrix[2], s_matrix[1]))
    elif s_cmd == "subtract":
        operate.subtract(s_matrix[0], get.matrix(s_matrix[2], s_matrix[1]))
    elif s_cmd == "multiply":
        operate.multiply(s_matrix[0], [s_matrix[1], s_matrix[2]])
    elif s_cmd == "divide":
        operate.divide(s_matrix[0], s_matrix[1])
    elif s_cmd == "compare":
        operate.compare(s_matrix[0], get.matrix(s_matrix[2], s_matrix[1]))