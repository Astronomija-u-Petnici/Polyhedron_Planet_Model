"""
Module for spherical linear interpolation (slerp) between two vectors.

This module provides the slerp function, which returns the uniform interpolation
of the arc defined by two vectors around the origin.
"""

import numpy as np

from scal_prod import scal_prod


def slerp(p0, p1, t):
    """
    Returns the uniform interpolation of the arc defined by p0 and p1 (around origin).

    Parameters
    ----------
    p0 : array-like
        Start vector.
    p1 : array-like
        End vector.
    t : float
        Interpolation parameter (0 -> p0, 1 -> p1).

    Returns
    -------
    out : ndarray
        Interpolated coordinates.

    Example
    -------
    >>> slerp([1,0,0], [0,1,0], 1)
    array([0., 1., 0.])
    """
    p0 = np.asarray(p0)
    p1 = np.asarray(p1)
    ang0_cos = scal_prod(p0, p1) / scal_prod(p0, p0)
    ang0_sin = np.sqrt(1 - ang0_cos * ang0_cos)
    ang0 = np.arctan2(ang0_sin, ang0_cos)

    l0 = np.sin((1 - t) * ang0)
    l1 = np.sin(t * ang0)

    out = (l0 * p0 + l1 * p1) / ang0_sin
    return out
