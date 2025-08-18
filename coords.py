"""
Module for computing barycentric coordinates for a specific triangle.

This module provides the barycentric_coords function, which returns the barycentric
coordinates for the triangle (-0.5,0), (0.5,0), (0,sqrt(3)/2).
"""


def barycentric_coords(p):
    """
    Returns the barycentric coordinates for the triangle
    (-0.5,0), (0.5,0), (0,sqrt(3)/2).

    Parameters
    ----------
    p : array-like
        Position vector of the form [x, y, 1].

    Returns
    -------
    l1, l2, l3 : float
        Barycentric coordinates.

    Example
    -------
    >>> barycentric_coords([1, 2, 1])
    (-1.6547..., 0.3453..., 2.3094...)
    """
    x = p[0]
    y = p[1]
    l3 = y * 2 / (3 ** 0.5)
    l2 = x + 0.5 * (1 - l3)
    l1 = 1 - l2 - l3
    return l1, l2, l3
