"""
You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

https://en.wikipedia.org/wiki/Triangle
"""

def other_angle(a, b):
    derajat_total = 180
    third_angle = derajat_total - (a + b)
    return third_angle