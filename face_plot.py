"""
Module for projecting and plotting a face onto the unit sphere.

This module provides the get_projected_face_plot function, which outputs and plots
the coordinates of a projected face on the plane defined by tips of the vectors u, v, and w
on the unit sphere.
"""
import numpy as np
from map_sphere import map_gidpoint_to_sphere
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def get_projected_face_plot(hexagon, u, v, w, ax=None):
    """
    Projects the input face (polygon) onto the unit sphere and plots it.

    Parameters
    ----------
    hexagon : ndarray
        Coordinate array of the planar vertices of the closed shape to be projected,
        shape (3, n) or (4, n).
    u, v, w : int
        Indices (0-based) of the vectors defining the plane to be projected on the sphere.
    ax : matplotlib 3d axis, optional
        If provided, plot on this axis.

    Returns
    -------
    face : ndarray
        Coordinate array of the projected face on the unit sphere, shape (3, n).
    """
    # Generate the corners (coordinates) of an icosahedron
    s = 2 / np.sqrt(5)
    c = 1 / np.sqrt(5)
    i = np.arange(5)
    top_points = np.vstack([
        np.zeros(5),
        s * np.cos(i * 2 * np.pi / 5),
        s * np.sin(i * 2 * np.pi / 5),
        c * np.ones(5)
    ]).T
    top_points = np.vstack([[0, 0, 1], top_points[:, 1:]])
    bottom_points = np.column_stack([-top_points[:, 0], top_points[:, 1], -top_points[:, 2]])
    ico_points = np.vstack([top_points, bottom_points])

    n = hexagon.shape[1]
    face = np.zeros((3, n))

    for idx in range(n):
        face[:, idx] = map_gidpoint_to_sphere(
            hexagon[:, idx],
            ico_points[u],
            ico_points[v],
            ico_points[w]
        )

    # Plotting
    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
    verts = [face.T]
    color = np.random.rand(3,)
    poly = Poly3DCollection(verts, alpha=0.3, facecolor=color, edgecolor='none')
    ax.add_collection3d(poly)
    ax.plot(
        face[0, :],
        face[1, :],
        face[2, :],
        '-',
        linewidth=2,
        color='k',
        marker='o',
        markerfacecolor='r',
        markeredgecolor='r',
        markersize=4
    )

    return face
