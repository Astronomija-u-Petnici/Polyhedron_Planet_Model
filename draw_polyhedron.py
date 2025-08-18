"""
Module for creating and plotting Goldberg Polyhedron (Geodesic Sphere of Hex and Pentagons)
of a given order n.

This script generates the Goldberg polyhedron and plots it in 3D using matplotlib.
"""

import numpy as np
from hexagon import hexagon
from face_plot import get_projected_face_plot
import matplotlib.pyplot as plt


def draw_goldberg_polyhedron(n):
    """
    Creates and plots a Goldberg Polyhedron (Geodesic Sphere of Hex and Pentagons)
    of given order n.

    Parameters
    ----------
    n : int
        Density of the grid (n >= 2 recommended).

    Returns
    -------
    None
    """
    x = -0.5
    y = 0

    i = np.arange(5)

    # Construct icosahedron triangle indices (1-based in MATLAB, 0-based in Python)
    ico_triangs = np.vstack([
        np.column_stack([np.zeros(5), i + 1, (np.mod(i + 1, 5) + 1)]),
        np.column_stack([np.full(5, 6), i + 7, (np.mod(i + 1, 5) + 7)]),
        np.column_stack([i + 1, (np.mod(i + 1, 5) + 1), (np.mod(7 - i, 5) + 7)]),
        np.column_stack([i + 1, (np.mod(7 - i, 5) + 7), (np.mod(8 - i, 5) + 7)])
    ]).astype(int)
    # Adjust for Python's 0-based indexing

    scale = 1 / (n * np.sqrt(3))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(n + 1):
        for j in range(n - i + 1):
            if i == 0:
                hex_type = 2
                th = -2 * np.pi / 3
            elif j == n - i:
                hex_type = 2
                th = 2 * np.pi / 3
            elif j == 0 and i != 0:
                hex_type = 2
                th = 0
            else:
                hex_type = 1
                th = 0

            if ((i != 0 or j != 0) and (i != 0 or j != n) and (i != n or j != 0)):
                hx = x + i * 1 / n + j * 1 / (2 * n)
                hy = y + j * (np.sqrt(3)) / (2 * n)
                hex_pts = hexagon(hx, hy, th, scale, hex_type)
                hex_pts_hom = np.vstack([hex_pts, np.ones(hex_pts.shape[1])])
                for k in range(ico_triangs.shape[0]):
                    a = ico_triangs[k, 0]
                    b = ico_triangs[k, 1]
                    c = ico_triangs[k, 2]
                    get_projected_face_plot(hex_pts_hom, a, b, c, ax=ax)

    ax.set_box_aspect([1, 1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
