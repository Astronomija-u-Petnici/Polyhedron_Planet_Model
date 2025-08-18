"""
Module for computing the scalar (dot) product of two 4D vectors.

This module provides the scal_prod function, which returns the scalar product
of two vectors of the form [x, y, z, 1].
"""

import numpy as np


def scal_prod(p1, p2):
    """
    Returns the scalar product of the input vectors p1 and p2.

    Parameters
    ----------
    p1 : array-like
        Vector of the form [x, y, z, 1].
    p2 : array-like
        Vector of the form [x, y, z, 1].

    Returns
    -------
    out : float
        Scalar product of p1 and p2.

    Example
    -------
    >>> scal_prod([1,2,3,1], [0.1,0.2,0.5,1])
    3.0
    """
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    return np.sum(p1 * p2)
