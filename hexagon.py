"""
Module for creating hexagons of various configurations and sizes.

This module provides the hexagon function, which creates a hexagon (full or partial)
with given center, rotation, scale, and hex_type.
"""

import numpy as np


def hexagon(x, y, th, scale, hex_type):
    """
    Creates a hexagon of given configuration and size.

    Parameters
    ----------
    x, y : float
        Rectangular coordinates of the center of the hexagon.
    th : float
        Rotation angle in radians, measured anticlockwise from positive x axis.
    scale : float
        Scaling factor for the hexagon.
    hex_type : int
        Type of hexagon:
            1 - full hexagon
            2 - half hexagon

    Returns
    -------
    hex : ndarray
        2 x N array of hexagon vertices.

    Example
    -------
    >>> hexagon(0, 0, np.pi/6, 0.5, 1)
    array([[...], [...]])
    """
    # Rotation matrix with scale
    rot_mat = scale * np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])

    if hex_type == 1:
        angles = np.arange(7) * 2 * np.pi / 6
        hex_pts = np.vstack((np.sin(angles), np.cos(angles)))
    elif hex_type == 2:
        sqrt3_2 = np.sqrt(3) / 2
        hex_pts = np.array([[sqrt3_2, sqrt3_2, 0, -sqrt3_2, -sqrt3_2], [0, 0.5, 1, 0.5, 0]])
    else:
        raise ValueError(f"Unsupported hexagon type: {hex_type}")

    hex_transformed = rot_mat @ hex_pts
    hex_transformed[0, :] += x
    hex_transformed[1, :] += y

    return hex_transformed
