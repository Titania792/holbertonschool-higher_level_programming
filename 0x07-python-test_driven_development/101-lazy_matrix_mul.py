#!/usr/bin/python3
"""function with NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """this function multiplies 2 matrices by using the module NumPy"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        for n in i:
            if not isinstance(n, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for n in i:
            if not isinstance(n, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    for i in m_a:
        if len(i) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for i in m_b:
        if len(i) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    try:
        return np.matmul(m_a, m_b)
    except ValueError:
        print("m_a and m_b can't be multiplied")
