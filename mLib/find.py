# Matrix Loves You : mLib/find.py

# Imports
from mLib import get, identify, operate, var
from packages import convert

# Functions
def transpose(t_matrix, t_option = None):
    t_new = list(())
    for t_each_col_index in range(t_matrix.get('col')):
        t_new_row = list(())
        for t_each_row_index in range(t_matrix.get('row')):
            t_new_row.append(t_matrix.get('value')[t_each_row_index][t_each_col_index])
        t_new.append(t_new_row)
    if t_option:
        return t_new
    else:
        print(convert.name(t_matrix.get('name') +"'", t_new))

def determinant(d_matrix, d_option = None):
    d_this = d_matrix.get('value')
    d_state = True
    if "One member matrix" in d_matrix.get('type'):
        d_value = d_this[0][0][0] / d_this[0][0][1]
    elif "Square matrix" in d_matrix.get('type'):
        if d_matrix.get('count') == var.detSize[0]:
            d_value = (d_this[0][0][0])/(d_this[0][0][1]) * (d_this[1][1][0])/(d_this[1][1][1]) - (d_this[0][1][0])/(d_this[0][1][1]) * (d_this[1][0][0])/(d_this[1][0][1])
        elif d_matrix.get('count') == var.detSize[1]:
            d_value_pos = (d_this[0][0][0]*d_this[1][1][0]*d_this[2][2][0])/(d_this[0][0][1]*d_this[1][1][1]*d_this[2][2][1]) + (d_this[0][1][0]*d_this[1][2][0]*d_this[2][0][0])/(d_this[0][1][1]*d_this[1][2][1]*d_this[2][0][1]) + (d_this[0][2][0]*d_this[1][0][0]*d_this[2][1][0])/(d_this[0][2][1]*d_this[1][0][1]*d_this[2][1][1])
            d_value_neg = (d_this[2][0][0]*d_this[1][1][0]*d_this[0][2][0])/(d_this[2][0][1]*d_this[1][1][1]*d_this[0][2][1]) + (d_this[2][1][0]*d_this[1][2][0]*d_this[0][0][0])/(d_this[2][1][1]*d_this[1][2][1]*d_this[0][0][1]) + (d_this[2][2][0]*d_this[1][0][0]*d_this[0][1][0])/(d_this[2][2][1]*d_this[1][0][1]*d_this[0][1][1])
            d_value = d_value_pos - d_value_neg
        elif d_matrix.get('count') in var.detSize[2:]:
            d_most = [[0, 0], [0, 0]]
            for d_each_row_index in range(len(d_this)):
                if d_this[d_each_row_index].count([0, 1]) > d_most[0][1]:
                    d_most[0][0] = d_each_row_index
                    d_most[0][1] = d_this[d_each_row_index].count([0, 1])
            d_transposted = transpose(d_matrix, True)
            for d_each_col_index in range(len(d_transposted)):
                if d_transposted[d_each_col_index].count([0, 1]) > d_most[1][1]:
                    d_most[1][0] = d_each_col_index
                    d_most[1][1] = d_transposted[d_each_col_index].count([0, 1])
            d_value = float()
            if d_most[0][1] >= d_most[1][1]:
                for d_irow_index in range(len(d_this[d_most[0][0]])):
                    d_value += get.member(d_matrix, d_most[0][0] + 1, d_irow_index + 1, True) * cofactor(d_matrix, d_most[0][0] + 1, d_irow_index + 1, True)
            elif d_most[0][1] < d_most[1][1]:
                for d_icol_index in range(len(d_transposted[d_most[1][0]])):
                    d_value += get.member(d_matrix, d_most[1][0] + 1, d_icol_index + 1, True) * cofactor(d_matrix, d_icol_index + 1, d_most[1][0] + 1, True)
        else:
            print("Info : Unable to find determinant of matrix bigger than 100 members, this protects your pc from lagging")
            d_state = False
    else:
        print("Error : Unable to find determinant of non square type matrix")
        d_state = False
    if type(d_value) == float and d_value.is_integer():
        d_value = int(d_value)
    if d_option:
        return d_value
    elif d_state:
        print("det("+ d_matrix.get('name') +") : "+ str(d_value))

def minor(m_matrix, m_i, m_j, m_option = None):
    if "Square matrix" in m_matrix.get('type'):
        if m_i > m_matrix.get('row') or m_j > m_matrix.get('col'):
            print("Error : member position out of index")
        elif m_i <= m_matrix.get('row') and m_j <= m_matrix.get('col'):
            m_new = list(())
            m_new_info = list(())
            for m_each_row_index in range(len(m_matrix.get('value'))):
                if m_each_row_index != m_i - 1:
                    m_new_row = m_matrix.get('value')[m_each_row_index]
                    m_new_info.append(m_matrix.get('value')[m_each_row_index][m_j - 1])
                    m_new_row.pop(m_j - 1)
                    m_new.append(m_new_row)
            m_new_matrix = dict(())
            m_new_matrix['name'] = identify.name(m_matrix.get('name'))
            m_new_matrix['value'] = m_new
            m_new_matrix['row'] = len(m_new)
            m_new_matrix['col'] = len(m_new[0])
            m_new_matrix['count'] = len(m_new)*len(m_new[0])
            m_new_matrix['call'] = convert.name(m_new_matrix.get('name'), m_new)
            m_new_matrix['type'] = identify.matrix(m_new_matrix)
            m_det = determinant(m_new_matrix, True)
            for m_each_row_index in range(len(m_matrix.get('value'))):
                if m_each_row_index != m_i - 1:
                    m_new_row = m_matrix.get('value')[m_each_row_index]
                    m_new_row.insert(m_j - 1, m_new_info[0])
                    m_new_info.pop(0)
            if m_option:
                return m_det
            else:
                print("minor("+ m_matrix.get('name') +", "+ str(m_i) +", "+ str(m_j) +") : "+ str(m_det))
        else:
            print("Error : unknown [mLib/find.py/minor()]")
    else:
        print("Error : Unable to find minor of non square type matrix")

def cofactor(c_matrix, c_i, c_j,  c_option = None):
    if "Square matrix" in c_matrix.get('type'):
        if c_i > c_matrix.get('row') or c_j > c_matrix.get('col'):
            print("Error : member position out of index")
        elif c_i <= c_matrix.get('row') and c_j <= c_matrix.get('col'):
            c_value = (-1) ** (c_i + c_j) * minor(c_matrix, c_i, c_j, True)
            if c_option:
                return c_value
            else:
                print("cofactor("+ c_matrix.get('name') +", "+ str(c_i) +", "+ str(c_j) +") : "+ str(c_value))
        else:
            print("Error : unknown [mLib/find.py/cofactor()]")
    else:
        print("Error : Unable to find co-factor of non square type matrix")

def inverse(i_matrix):
    if "One member matrix" in i_matrix.get('type'):
        print("inverse("+ i_matrix.get('name') +") : [ 1 ]")
    elif "Square matrix" in i_matrix.get('type'):
        i_det = determinant(i_matrix, True)
        if i_det != 0:
            i_new_list = list(())
            for i_each_row_index in range(i_matrix.get('row')):
                i_make_matrix = list(())
                for i_each_col_index in range(i_matrix.get('col')):
                    i_new_value = i_matrix.get('value')[i_each_row_index][i_each_col_index]
                    if i_each_row_index != i_each_col_index:
                        i_make_matrix.append([i_new_value[0] * (-1), i_new_value[1]])
                i_new_list.append(i_make_matrix)
            for i_each_row_index in range(i_matrix.get('row')):
                for i_each_col_index in range(i_matrix.get('col')):
                    i_new_value = i_matrix.get('value')[i_each_row_index][i_each_col_index]
                    if i_each_row_index == i_each_col_index:
                        i_new_list[i_matrix.get('row') - i_each_row_index - 1].insert(i_matrix.get('col') - i_each_col_index - 1, i_new_value)
            i_new_matrix = dict(())
            i_new_matrix['name'] = identify.name(i_matrix.get('name'))
            i_new_matrix['value'] = i_new_list
            i_new_matrix['row'] = len(i_new_list)
            i_new_matrix['col'] = len(i_new_list[0])
            i_new_matrix['count'] = len(i_new_list)*len(i_new_list[0])
            i_new_matrix['type'] = identify.matrix(i_new_matrix)
            i_new_inverse = operate.divide(i_new_matrix, i_det, True)
            i_new_name = ("inverse("+ i_matrix.get('name') +")")
            i_new_matrix['call'] = convert.name(i_new_name, i_new_inverse)
            print(i_new_matrix.get('call'))
        elif i_det == 0:
            print("Error : Unable to find inverse, divided by zero")