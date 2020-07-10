# Matrix Loves You : mLib/get.py

# Functions
def matrix(m_store, m_name):
    for each_matrix in m_store:
        if each_matrix.get('name') == m_name.upper():
            return each_matrix
            break

def allvar(a_all):
    a_names = list(())
    for each_matrix in a_all:
        a_names.append(each_matrix.get('name'))
    return a_names

def value(v_matrix):
    print(v_matrix.get('call'))

# def category(c_matrix):
#     print("type("+ c_matrix.get('name') +") : "+ c_matrix.get('type'))

# def dimension(d_matrix):
#     print("dim("+ d_matrix.get('name') +") : "+ str(d_matrix.get('col')) +u" \u00D7 "+ str(d_matrix.get('row')))

# def amount(a_matrix):
#     print("count("+ a_matrix.get('name') +") : "+ str(a_matrix.get('count')))

def member(m_matrix, m_i, m_j, m_option = None):
    if m_i > m_matrix.get('row') or m_j > m_matrix.get('col'):
        print("Error : member position out of index")
    elif m_i <= m_matrix.get('row') and m_j <= m_matrix.get('col'):
        m_value = m_matrix.get('value')[m_i - 1][m_j - 1][0] / m_matrix.get('value')[m_i - 1][m_j - 1][1]
        if m_value.is_integer():
            m_value = int(m_value)
        if m_option:
            return m_value
        else:
            print("member("+ m_matrix.get('name') +", "+ str(m_i) +", "+ str(m_j) +") : "+ str(m_value))
    else:
        print("Error : unknown [mLib/get.py/member()]")

def property(p_matrix):
    print("Name :", p_matrix.get('name'))
    print("Dimension :", p_matrix.get('row'), "x", p_matrix.get('col'), "(row x column)")
    print("Amt of member :", p_matrix.get('count'))
    print("Matrix type :", p_matrix.get('type'))
    # print(p_matrix.get('call'))