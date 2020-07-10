# Matrix Loves You : push/cramer.py

# Imports
from mLib import find, get, identify, var
from packages import convert
from fractions import Fraction as fnd

# Functions
def cInput():
    print("\nPlease enter expressions below (Variables on the left, real numbers on the right. Only use + as seperator)")
    a_algebra_store = list(())
    a_length_extend = "0123456789"
    for a_algebra_require in range(len(a_length_extend)):
        a_get_input = input("Expression ("+ str(len(a_algebra_store) + 1) +") : ")
        if a_get_input == "" and len(a_algebra_store) >= 2:
            break
        elif a_get_input == "" and len(a_algebra_store) < 2:
            print("Error : Please enter at least 2 expressions")
        else:
            a_set_pass = set(())
            for a_each_require in var.Expsymbol:
                if a_each_require in a_get_input:
                    a_set_pass.add(True)
                else:
                    a_set_pass.add(False)
            if False not in a_set_pass:
                a_algebra_store.append(a_get_input)
            else:
                print("Error : Expression doesn't contains required character")
                a_length_extend += "."
    return a_algebra_store

def cConvert(c_data):
    c_store = c_data
    # Find all vars
    c_set_vars = set(())
    for c_each_expression in c_store:
        c_esplit = "="
        c_asplit = "+"
        if c_each_expression[c_each_expression.index("=") - 1] == " ":
            c_esplit = " = "
        if c_each_expression[c_each_expression.index("+") - 1] == " ":
            c_asplit = " + "
        c_value = c_each_expression.split(c_esplit)[0].split(c_asplit)
        c_value.append(c_each_expression.split(c_esplit)[1])
        for c_each_section in c_value:
            for c_each_char in c_each_section:
                if c_each_char.lower() in var.Lowercase:
                    c_set_vars.add(c_each_char)
    if len(c_set_vars) != len(c_store):
        print("Error : Amount of expressions is inequal to amount of variables")
        c_return = "error"
    else:
        c_splited = list(())
        c_matrix_equal = list(())
        for c_each_expression in c_store:
            c_esplit = "="
            c_asplit = "+"
            if c_each_expression[c_each_expression.index("=") - 1] == " ":
                c_esplit = " = "
            if c_each_expression[c_each_expression.index("+") - 1] == " ":
                c_asplit = " + "
            c_splited.append(c_each_expression.split(c_esplit)[0].split(c_asplit))
            c_matrix_equal.append([c_each_expression.split(c_esplit)[1]])
        del c_each_expression
        c_list_vars = list(c_set_vars)
        c_list_vars.sort()
        c_matrix_transposed = list(())
        for c_each_var in c_list_vars:
            c_each_row = list(())
            for c_each_expression in c_splited:
                c_find = True
                for c_each_part in c_each_expression:
                    if c_each_var in c_each_part:
                        if len(c_each_part) == 1:
                            c_each_row.append("1")
                            c_find = False
                            break
                        elif len(c_each_part) == 2 and c_each_part[0] == "-":
                            c_each_row.append("-1")
                            c_find = False
                            break
                        else:
                            c_each_row.append(c_each_part[:-1])
                            c_find = False
                            break
                if c_find:
                    c_each_row.append("0")
            c_matrix_transposed.append(c_each_row)
        c_matrix = convert.data({"A" : c_matrix_transposed, "B" : c_matrix_equal})
        c_matrix[0]['value'] = find.transpose(get.matrix(c_matrix, "A"), True)
        c_return = [get.matrix(c_matrix, "A"), get.matrix(c_matrix, "B"), c_list_vars]
    return c_return

def cFind(f_data):
    if f_data != "error":
        f_main = f_data[0]
        f_replace = f_data[1]
        f_variable = f_data[2]
        f_det_main = find.determinant(f_main, True)
        if f_det_main == 0:
            print("Expression is not true!")
        else:
            f_store_new = dict(())
            for f_each_var_index, f_each_var in enumerate(f_variable):
                f_new_matrix = list(())
                for f_each_row_index, f_each_row in enumerate(f_main.get('value')):
                    f_new_row = list(())
                    for f_each_col_index, f_each_col in enumerate(f_each_row):
                        if f_each_col_index == f_each_var_index:
                            f_new_row.append(f_replace.get('value')[f_each_row_index][0])
                        else:
                            f_new_row.append(f_each_col)
                    f_new_matrix.append(f_new_row)
                f_store_new[f_each_var.upper()] = f_new_matrix
            for f_get_var in f_variable:
                f_get_new_matrix = dict(())
                f_get_new_matrix['name'] = identify.name(f_get_var.upper())
                f_get_new_matrix['value'] = f_store_new.get(f_get_var.upper())
                f_get_new_matrix['row'] = len(f_store_new.get(f_get_var.upper()))
                f_get_new_matrix['col'] = len(f_store_new.get(f_get_var.upper())[0])
                f_get_new_matrix['count'] = len(f_store_new.get(f_get_var.upper()))*len(f_store_new.get(f_get_var.upper())[0])
                f_get_new_matrix['call'] = convert.name(f_get_var.upper(), f_store_new.get(f_get_var.upper()))
                f_get_new_matrix['type'] = identify.matrix(f_get_new_matrix)
                f_det_me = find.determinant(f_get_new_matrix, True)
                f_value = f_det_me / f_det_main
                if type(f_value) == float and f_value.is_integer() or type(f_value) == int:
                    f_value = int(f_value)
                else:
                    f_value = str(fnd(float(f_value)).limit_denominator())
                print(f_get_var +" = "+ str(f_value))