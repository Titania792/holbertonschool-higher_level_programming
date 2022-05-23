#!/usr/bin/python3
"""function that multiplies 2 matrices"""
import numpy as np


def matrix_mul(m_a, m_b):
    """this function multiplies 2 matrices"""
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
        result = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]
        for i in range(len(result)):
            for j in range(len(result[i])):
                for a in range(len(m_b)):
                    result[i][j] += m_a[i][a] * m_b[a][j]
        return result
    except ValueError:
        print("m_a and m_b can't be multiplied")
