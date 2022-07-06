import math
import numpy as np


def translate(pos):
    tx, ty, tz = pos
    # mat = np.eye(4, 4)
    # mat[-1][0] = tx
    # mat[-1][1] = ty
    # mat[-1][2] = tz
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [tx,ty,tz,1]
    ])


def rotate_x(phi):
    return np.array([
        [1, 0, 0, 0], 
        [0, math.cos(phi), math.sin(phi), 0],
        [0,-math.sin(phi), math.cos(phi), 0], 
        [0, 0, 0, 1]
    ])


def rotate_y(phi):
    return np.array([
        [math.cos(phi),0,-math.sin(phi), 0],
        [0, 1, 0, 0], 
        [math.sin(phi), 0, math.cos(phi), 0],
        [0, 0, 0, 1]
    ])


def rotate_z(phi):
    return np.array([
        [ math.cos(phi), math.sin(phi), 0, 0],
        [-math.sin(phi), math.cos(phi), 0, 0],
        [0, 0, 1, 0], 
        [0, 0, 0, 1]
    ])


def scale(a):
    # mat = np.eye(4, 4) * a
    # mat[-1][-1] = 1
    return np.array([
        [a, 0, 0, 0],
        [0, a, 0, 0],
        [0, 0, a, 0],
        [0, 0, 0, 1]
    ])