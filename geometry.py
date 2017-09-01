
# This program contains functions that evaluate formulas used in geometry.
#
# Your Name
# August 22, 2014

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

def parallelogram_area (b, h):
    a = b * h
    return a

def trapezoid_area (b, a, h):
    A = ( a+ b / 2) * h
    return  A

def rectangular_prism_volume (w, h, l):
    a = w * h * l
    return a

def cone_volume(r, h):
    a = (math.pi * r ** 2) * (h / 3)
    return a

def sphere_volume(r):
    a = 4 / 3 * math.pi * r ** 3
    return a

def rectangular_prism_suface_area(w, l, h):
    a = 2 * (w * l + h * l + h * w)
    return a

def sphere_surface_area(r):
    a = 4 * math.pi * r ** 2
    return a

def triangle_hypo(b, c):
    a = (b**2 + c**2)** .5
    return a

def triangle_area2(a, b, c) :
    s = (a + b + c) / 2
    z = (s * (s - a) * (s - b) * (s - c)) ** .5
    return z





# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))
print(parallelogram_area(4,8))
print(trapezoid_area(4,2,8))
print(rectangular_prism_volume(4,8,5))
print(cone_volume(4,2))
print(sphere_volume(4))
print( rectangular_prism_suface_area(4,2,8))
print(sphere_surface_area(4))
print(triangle_hypo(4,3))
print(triangle_area2(3,5,7))
