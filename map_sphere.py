"""
Module for projecting planar coordinates onto the unit sphere.

This module provides the map_gidpoint_to_sphere function, which projects
planar coordinates onto the unit sphere using barycentric coordinates and
spherical linear interpolation.
"""

import numpy as np

from coords import barycentric_coords
from slerp import slerp


def map_gidpoint_to_sphere(p, s1, s2, s3):
    """
    Projects the input planar coordinates onto the unit sphere.

    Parameters
    ----------
    p : array-like
        Coordinate array of the planar vertex [x, y, z, 1] or [x, y, 1].
    s1, s2, s3 : array-like
        Vectors defining the plane of the coordinates to be projected.

    Returns
    -------
    out : ndarray
        Coordinate array of the projected face on the unit sphere.

    Example
    -------
    >>> map_gidpoint_to_sphere([0, 0.5, 0.5], [1,0,0], [0,1,0], [0,0,1])
    array([0.4357..., 0.4357..., 0.7876...])
    """
    l1, l2, l3 = barycentric_coords(p)

    if abs(l3 - 1) < 1e-10:
        out = np.asarray(s3)
    else:
        l2s = l2 / (l1 + l2)
        p12 = slerp(s1, s2, l2s)
        out = slerp(p12, s3, l3)
    return out
