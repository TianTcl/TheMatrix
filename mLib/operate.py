# Matrix Loves You : mLib/operate.py

# Imports
from mLib import get, var
from packages import convert
from fractions import Fraction as fnd

# Functions
def add(a_one, a_two):
    if a_one.get('row') == a_two.get('row') and a_one.get('col') == a_two.get('col'):
        a_new_matrix = list(())
        for a_each_row in range(a_one.get('row')):
            a_new_member = list(())
            for a_each_col in range(a_one.get('col')):
                a_new_value = a_one.get('value')[a_each_row][a_each_col][0]/a_one.get('value')[a_each_row][a_each_col][1] + a_two.get('value')[a_each_row][a_each_col][0]/a_two.get('value')[a_each_row][a_each_col][1]
                if type(a_new_value) == float and a_new_value.is_integer() or type(a_new_value) == int:
                    a_new_value = [int(a_new_value), 1]
                else:
                    a_new_value = str(fnd(float(a_new_value)).limit_denominator()).split("/")
                    a_new_value = [int(a_new_value[0]), int(a_new_value[1])]
                a_new_member.append(a_new_value)
            a_new_matrix.append(a_new_member)
        a_new_name = (a_one.get('name') +" + "+ a_two.get('name'))
        print(convert.name(a_new_name, a_new_matrix))
    else:
        print("Error : Unable to add matrixes with different dimensions")

def subtract(s_one, s_two):
    if s_one.get('row') == s_two.get('row') and s_one.get('col') == s_two.get('col'):
        s_new_matrix = list(())
        for s_each_row in range(s_one.get('row')):
            s_new_member = list(())
            for s_each_col in range(s_one.get('col')):
                s_new_value = s_one.get('value')[s_each_row][s_each_col][0]/s_one.get('value')[s_each_row][s_each_col][1] - s_two.get('value')[s_each_row][s_each_col][0]/s_two.get('value')[s_each_row][s_each_col][1]
                if type(s_new_value) == float and s_new_value.is_integer() or type(s_new_value) == int:
                    s_new_value = [int(s_new_value), 1]
                else:
                    s_new_value = str(fnd(float(s_new_value)).limit_denominator()).split("/")
                    s_new_value = [int(s_new_value[0]), int(s_new_value[1])]
                s_new_member.append(s_new_value)
            s_new_matrix.append(s_new_member)
        s_new_name = (s_one.get('name') +" - "+ s_two.get('name'))
        print(convert.name(s_new_name, s_new_matrix))
    else:
        print("Error : Unable to add matrixes with different dimensions")

def multiply(m_one, m_two):
    if type(m_two[0]) == str:
        m_two = get.matrix(m_two[1], m_two[0])
        if m_one.get('col') == m_two.get('row'):
            m_new_matrix = list(())
            for m_each_row_index in range(m_one.get('row')):
                m_new_row = list(())
                for m_each_col_index in range(m_two.get('col')):
                    m_new_member = 0
                    for m_each_mem_index in range(m_one.get('col')):
                        m_new_member += m_one.get('value')[m_each_row_index][m_each_mem_index][0]/m_one.get('value')[m_each_row_index][m_each_mem_index][1] * m_two.get('value')[m_each_mem_index][m_each_col_index][0]/m_two.get('value')[m_each_mem_index][m_each_col_index][1]
                    if type(m_new_member) == float and m_new_member.is_integer() or type(m_new_member) == int:
                        m_new_member = [int(m_new_member), 1]
                    else:
                        m_new_member = str(fnd(float(m_new_member)).limit_denominator()).split("/")
                        m_new_member = [int(m_new_member[0]), int(m_new_member[1])]
                    m_new_row.append(m_new_member)
                m_new_matrix.append(m_new_row)
            m_new_name = m_one.get('name') + m_two.get('name')
            print(convert.name(m_new_name, m_new_matrix))
        else:
            print("Error : Unable to multiply matrixes, dimension does not match")
    elif type(m_two[0]) == list:
        m_two = m_two[0]
        m_new_matrix = list(())
        for m_each_row in range(m_one.get('row')):
            m_new_member = list(())
            for m_each_col in range(m_one.get('col')):
                m_new_value = m_one.get('value')[m_each_row][m_each_col][0]/m_one.get('value')[m_each_row][m_each_col][1] * m_two[0]/m_two[1]
                if type(m_new_value) == float and m_new_value.is_integer() or type(m_new_value) == int:
                    m_new_value = [int(m_new_value), 1]
                else:
                    m_new_value = str(fnd(float(m_new_value)).limit_denominator()).split("/")
                    m_new_value = [int(m_new_value[0]), int(m_new_value[1])]
                m_new_member.append(m_new_value)
            m_new_matrix.append(m_new_member)
        m_multiplier = m_two[0]/m_two[1]
        if type(m_multiplier) == float and m_multiplier.is_integer() or type(m_multiplier) == int:
            m_multiplier = int(m_multiplier)
        m_new_name = (str(m_multiplier) +"("+ m_one.get('name') +")")
        print(convert.name(m_new_name, m_new_matrix))

def divide(d_one, d_two, d_option = None):
    d_new_matrix = list(())
    if type(d_two) == int or type(d_two) == float:
        d_divisor = d_two
    elif type(d_two) == list:
        d_divisor = d_two[0]/d_two[1]
    for d_each_row in range(d_one.get('row')):
        d_new_member = list(())
        for d_each_col in range(d_one.get('col')):
            d_new_value = d_one.get('value')[d_each_row][d_each_col][0]/d_one.get('value')[d_each_row][d_each_col][1] / d_divisor
            if type(d_new_value) == float and d_new_value.is_integer() or type(d_new_value) == int:
                d_new_value = [int(d_new_value), 1]
            else:
                d_new_value = str(fnd(float(d_new_value)).limit_denominator()).split("/")
                d_new_value = [int(d_new_value[0]), int(d_new_value[1])]
            d_new_member.append(d_new_value)
        d_new_matrix.append(d_new_member)
    if type(d_divisor) == float and d_divisor.is_integer() or type(d_divisor) == int:
            d_divisor = int(d_divisor)
    d_new_name = (d_one.get('name') +"/"+ str(d_divisor))
    if d_option:
        return d_new_matrix
    else:
        print(convert.name(d_new_name, d_new_matrix))

def compare(c_one, c_two):
    if c_one.get('row') == c_two.get('row'):
        if c_one.get('col') == c_two.get('col'):
            c_set_rs = set(())
            for c_each_row in range(c_one.get('row')):
                for c_each_col in range(c_one.get('col')):
                    if c_one.get('value')[c_each_row][c_each_col][0]/c_one.get('value')[c_each_row][c_each_col][1] == c_two.get('value')[c_each_row][c_each_col][0]/c_two.get('value')[c_each_row][c_each_col][1]:
                        c_set_rs.add(True)
                    else:
                        c_set_rs.add(False)
            if False not in c_set_rs:
                c_message = str("Matrix '"+ c_one.get('name') +"' is equal to matrix '"+ c_two.get('name') +"'")
            else:
                c_message = str("Matrix '"+ c_one.get('name') +"' is not equal to matrix '"+ c_two.get('name') +"' | Members")
        else:
            c_message = str("Matrix '"+ c_one.get('name') +"' is not equal to matrix '"+ c_two.get('name') +"' | Columns")
    else:
        c_message = str("Matrix '"+ c_one.get('name') +"' is not equal to matrix '"+ c_two.get('name') +"' | Rows")
    c_prefix = str("Compare("+ c_one.get('name') +", "+ c_two.get('name') +") :\t")
    print(c_prefix + c_message)