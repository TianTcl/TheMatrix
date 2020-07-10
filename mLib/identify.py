# Matrix Loves You : mLib/identify.py

# Imports
from mLib import var

# Functions
def matrix(m_matrix):
    m_dev_type = ""
    m_dev_find = True
    # Matrix : Square
    if m_dev_find:
        if m_matrix.get('row') == m_matrix.get('col') and m_matrix.get('row') != 1 and m_matrix.get('col') != 1:
            m_dev_type += "Square matrix"
    # Matrix : Upper triangular
    if m_dev_find:
        if m_matrix.get('row') == m_matrix.get('col') and m_matrix.get('row') != 1 and m_matrix.get('col') != 1:
            m_upper_set_m = set(())
            m_upper_set_o = set(())
            for m_upper_row_index, m_upper_row in enumerate(m_matrix.get('value')):
                for m_upper_col_index, m_upper_col in enumerate(m_upper_row):
                    if m_upper_row_index > m_upper_col_index:
                        m_upper_set_m.add(m_upper_col[0] / m_upper_col[1])
                    else:
                        m_upper_set_o.add(m_upper_col[0] / m_upper_col[1])
            m_upper_rs_m = len(m_upper_set_m) == 1 and 0 in m_upper_set_m
            m_upper_rs_o = (len(m_upper_set_o) == 1 and 0 not in m_upper_set_o) or (len(m_upper_set_o) >= 1)
            if m_upper_rs_m and m_upper_rs_o:
                if m_dev_type != "":
                    m_dev_type += ", "
                m_dev_type += "Upper triangular matrix"
    # Matrix : Lower triangular
    if m_dev_find:
        if m_matrix.get('row') == m_matrix.get('col') and m_matrix.get('row') != 1 and m_matrix.get('col') != 1:
            m_lower_set_m = set(())
            m_lower_set_o = set(())
            for m_lower_row_index, m_lower_row in enumerate(m_matrix.get('value')):
                for m_lower_col_index, m_lower_col in enumerate(m_lower_row):
                    if m_lower_row_index < m_lower_col_index:
                        m_lower_set_m.add(m_lower_col[0] / m_lower_col[1])
                    else:
                        m_lower_set_o.add(m_lower_col[0] / m_lower_col[1])
            m_lower_rs_m = len(m_lower_set_m) == 1 and 0 in m_lower_set_m
            m_lower_rs_o = (len(m_lower_set_o) == 1 and 0 not in m_lower_set_o) or (len(m_lower_set_o) >= 1)
            if m_lower_rs_m and m_lower_rs_o:
                if m_dev_type != "":
                    m_dev_type += ", "
                m_dev_type += "Lower triangular matrix"
    # Matrix : 0
    if m_dev_find:
        m_zero_set = set(())
        for m_zero_row in m_matrix.get('value'):
            for m_zero_col in m_zero_row:
                m_zero_set.add(m_zero_col[0] / m_zero_col[1])
        if len(m_zero_set) == 1 and 0 in m_zero_set:
            if m_dev_type != "":
                m_dev_type += ", "
            m_dev_type += "Zero matrix"
            m_dev_find = False
    # Matrix : Diagonal
    if m_dev_find:
        if m_matrix.get('row') == m_matrix.get('col') and m_matrix.get('row') != 1 and m_matrix.get('col') != 1:
            m_diagonal_set_o = set(())
            for m_diagonal_row_index, m_diagonal_row in enumerate(m_matrix.get('value')):
                for m_diagonal_col_index, m_diagonal_col in enumerate(m_diagonal_row):
                    if m_diagonal_row_index != m_diagonal_col_index:
                        m_diagonal_set_o.add(m_diagonal_col[0] / m_diagonal_col[1])
            if len(m_diagonal_set_o) == 1 and 0 in m_diagonal_set_o:
                if m_dev_type != "":
                    m_dev_type += ", "
                m_dev_type += "Diagonal matrix"
    # Matrix : Identity
    if m_dev_find:
        if m_matrix.get('row') == m_matrix.get('col') and m_matrix.get('row') != 1 and m_matrix.get('col') != 1:
            m_identity_set_o = set(())
            m_identity_set_d = set(())
            for m_identity_row_index, m_identity_row in enumerate(m_matrix.get('value')):
                for m_identity_col_index, m_identity_col in enumerate(m_identity_row):
                    if m_identity_row_index == m_identity_col_index:
                        m_identity_set_d.add(m_identity_col[0] / m_identity_col[1])
                    elif m_identity_row_index != m_identity_col_index:
                        m_identity_set_o.add(m_identity_col[0] / m_identity_col[1])
            m_identity_rs_d = len(m_identity_set_d) == 1 and 1 in m_identity_set_d
            m_identity_rs_o = len(m_identity_set_o) == 1 and 0 in m_identity_set_o
            if m_identity_rs_d and m_identity_rs_o:
                if m_dev_type != "":
                    m_dev_type += ", "
                m_dev_type += "Identity matrix"
                m_dev_find = False
    # Matrix : Scalar
    if m_dev_find:
        if m_matrix.get('row') == m_matrix.get('col') and m_matrix.get('row') != 1 and m_matrix.get('col') != 1:
            m_scalar_set_o = set(())
            m_scalar_set_d = set(())
            for m_scalar_row_index, m_scalar_row in enumerate(m_matrix.get('value')):
                for m_scalar_col_index, m_scalar_col in enumerate(m_scalar_row):
                    if m_scalar_row_index == m_scalar_col_index:
                        m_scalar_set_d.add(m_scalar_col[0] / m_scalar_col[1])
                    elif m_scalar_row_index != m_scalar_col_index:
                        m_scalar_set_o.add(m_scalar_col[0] / m_scalar_col[1])
            m_scalar_rs_d = len(m_scalar_set_d) == 1 and 1 not in m_scalar_set_d
            m_scalar_rs_o = len(m_scalar_set_o) == 1 and 0 in m_scalar_set_o
            if m_scalar_rs_d and m_scalar_rs_o:
                if m_dev_type != "":
                    m_dev_type += ", "
                m_dev_type += "Scalar matrix"
                m_dev_find = False
    # Matrix : Symmetric
    if m_dev_find:
        m_symmetric_set = set(())
        if m_matrix.get('row') == m_matrix.get('col') and m_matrix.get('row') != 1 and m_matrix.get('col') != 1:
            for m_symmetric_row in range(m_matrix.get('row')):
                for m_symmetric_col in range(m_matrix.get('col')):
                    m_symmetric_con_i = m_symmetric_row < m_symmetric_col
                    m_symmetric_con_n = (m_matrix.get('value')[m_symmetric_row][m_symmetric_col][0] / m_matrix.get('value')[m_symmetric_row][m_symmetric_col][1]) == (m_matrix.get('value')[m_symmetric_col][m_symmetric_row][0] / m_matrix.get('value')[m_symmetric_col][m_symmetric_row][1])
                    if m_symmetric_con_i and m_symmetric_con_n:
                        m_symmetric_set.add(True)
                    elif m_symmetric_con_i and not m_symmetric_con_n:
                        m_symmetric_set.add(False)
            if len(m_symmetric_set) == 1 and False not in m_symmetric_set:
                if m_dev_type != "":
                    m_dev_type += ", "
                m_dev_type += "Symmetric matrix"
                m_dev_find = False
    # Matrix : Skew symmetric
    if m_dev_find:
        m_skew_set = set(())
        if m_matrix.get('row') == m_matrix.get('col') and m_matrix.get('row') != 1 and m_matrix.get('col') != 1:
            for m_skew_row in range(m_matrix.get('row')):
                for m_skew_col in range(m_matrix.get('col')):
                    m_skew_con_i = m_skew_row < m_skew_col
                    m_skew_con_n = (m_matrix.get('value')[m_skew_row][m_skew_col][0] / m_matrix.get('value')[m_skew_row][m_skew_col][1]) == (m_matrix.get('value')[m_skew_col][m_skew_row][0] / m_matrix.get('value')[m_skew_col][m_skew_row][1]) * -1
                    if m_skew_con_i and m_skew_con_n:
                        m_skew_set.add(True)
                    elif m_skew_con_i and not m_skew_con_n:
                        m_skew_set.add(False)
            if len(m_skew_set) == 1 and False not in m_skew_set:
                if m_dev_type != "":
                    m_dev_type += ", "
                m_dev_type += "Skew symmetric matrix"
                m_dev_find = False
    # Matrix : Row
    if m_dev_find:
        if m_matrix.get('row') == 1 and m_matrix.get('col') != 1:
            m_dev_type += "Row matrix"
            m_dev_find = False
    # Matrix : Col
    if m_dev_find:
        if m_matrix.get('col') == 1 and m_matrix.get('row') != 1:
            m_dev_type += "Column matrix"
            m_dev_find = False
    # Matrix : Unit
    if m_dev_find:
        if m_matrix.get('row') == 1 and m_matrix.get('col') == 1:
            m_dev_type += "One member matrix"
            m_dev_find = False
    # Clean result
    if m_dev_type == "":
        m_dev_type = "Normal matrix"
    return m_dev_type

def name(n_old):
    if len(n_old) == 1:
        n_new = n_old +"0"
    elif len(n_old) == 2:
        n_new = n_old[0] + var.Integer[var.Integer.index(n_old[1]) + 1]
    else:
        print("Error : Iterating name too long")
        n_new = n_old[0] + "OL"
    return n_new        