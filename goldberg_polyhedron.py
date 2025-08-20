"""
Module for Goldberg Polyhedron construction and plotting.
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Cell:
    """
    Class representing a cell in the Goldberg Polyhedron.
    """

    def __init__(self, vertices, cell_type=None, neighbors=None):
        """
        Initializes the Cell with given vertices.

        Parameters
        ----------
        vertices : list of tuples
            List of vertices defining the cell.
        """
        self.cell_type = cell_type if cell_type is not None else None
        self.vertices = np.array(vertices)
        self._round_vertices()
        self._remove_extra_vertices()
        self.center = np.mean(self.vertices, axis=0)
        self.normal = np.cross(
            self.vertices[1] - self.vertices[0], self.vertices[2] - self.vertices[0]
        )
        self.neighbors = neighbors if neighbors is not None else set()

    def __repr__(self):
        """
        String representation of the Cell object.

        Returns
        -------
        str
            String representation of the Cell.
        """
        return f"Cell(type={self.cell_type}, vertices={self.vertices})"

    def set_cell_type(self, cell_type):
        """
        Sets the type of the cell.

        Parameters
        ----------
        cell_type : str
            Type of the cell (e.g., 'hexagon', 'pentagon', 'half_hexagon').
        """
        self.cell_type = cell_type

    def find_center(self):
        """
        Finds the center of the cell based on its vertices.
        """
        self.center = np.mean(self.vertices, axis=0)

    def _remove_extra_vertices(self):
        """
        Removes extra verices of the hexagonal cell.
        """
        if self.vertices.shape[0] > 6:
            self.vertices = self.vertices[:6, :]

    def _round_vertices(self):
        """
        Rounds the vertices to 4 decimal places.
        """
        self.vertices = np.round(self.vertices, 4)


class GoldbergPolyhedron:
    """
    Class representing a Goldberg Polyhedron (Geodesic Sphere of Hex and Pentagons).
    """

    def __init__(self, center=(0, 0, 0), order=2, radius=1):
        """
        Initializes the GoldbergPolyhedron with a center and order.

        Parameters
        ----------
        center : tuple
            Center of the polyhedron in 3D space (x, y, z).
        order : int
            Order of the Goldberg Polyhedron.
        """
        self.cells = []
        self.center = np.array(center)
        self.order = order
        self.radius = radius
        self._create_goldberg_polyhedron(self.order, self.center, self.radius)

    def __repr__(self):
        """
        String representation of the GoldbergPolyhedron object.

        Returns
        -------
        str
            String representation of the GoldbergPolyhedron.
        """
        return f"GoldbergPolyhedron(center={self.center}, order={self.order})"

    def draw_goldberg_polyhedron(self):
        """
        Plots a Goldberg Polyhedron (Geodesic Sphere of Hex and Pentagons)
        of given order n.
        """
        self._create_goldberg_polyhedron(
            self.order, self.center, self.radius, plot=True, create_cells=False
        )

    def plot(self):
        """
        Plots the Goldberg Polyhedron using matplotlib.
        """
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection="3d")

        all_verts = np.concatenate([np.array(cell.vertices) for cell in self.cells])
        max_range = (all_verts.max(axis=0) - all_verts.min(axis=0)).max() / 2.0
        mid_x = (all_verts[:, 0].max() + all_verts[:, 0].min()) * 0.5
        mid_y = (all_verts[:, 1].max() + all_verts[:, 1].min()) * 0.5
        mid_z = (all_verts[:, 2].max() + all_verts[:, 2].min()) * 0.5

        for cell in self.cells:
            verts = np.array(cell.vertices)
            if not np.allclose(verts[0], verts[-1]):
                verts = np.vstack([verts, verts[0]])
            poly = Poly3DCollection([verts], alpha=0.6)
            poly.set_facecolor(
                np.random.rand(
                    3,
                )
            )
            poly.set_edgecolor("k")
            ax.add_collection3d(poly)

        ax.set_xlim(mid_x - max_range, mid_x + max_range)
        ax.set_ylim(mid_y - max_range, mid_y + max_range)
        ax.set_zlim(mid_z - max_range, mid_z + max_range)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.tight_layout()
        plt.show()

    def _create_goldberg_polyhedron(
        self, n, center=(0, 0, 0), radius=1, plot=False, create_cells=True
    ):
        """
        Creates and optionally plots a Goldberg Polyhedron
        (Geodesic Sphere of Hex and Pentagons) of given order.

        Parameters
        ----------
        n : int
            Order of the Goldberg Polyhedron.
        center : tuple, optional
            Center of the polyhedron in 3D space (x, y, z). Default is (0, 0, 0).
        plot : bool, optional
            If True, the polyhedron will be plotted. Default is False.
        """
        x = -0.5
        y = 0

        i = np.arange(5)

        ico_triangs = np.vstack(
            [
                np.column_stack([np.zeros(5), i + 1, (np.mod(i + 1, 5) + 1)]),
                np.column_stack([np.full(5, 6), i + 7, (np.mod(i + 1, 5) + 7)]),
                np.column_stack([i + 1, (np.mod(i + 1, 5) + 1), (np.mod(7 - i, 5) + 7)]),
                np.column_stack([i + 1, (np.mod(7 - i, 5) + 7), (np.mod(8 - i, 5) + 7)]),
            ]
        ).astype(int)

        scale = 1 / (n * np.sqrt(3))

        if plot:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")
        else:
            ax = None

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

                if (i != 0 or j != 0) and (i != 0 or j != n) and (i != n or j != 0):
                    hx = x + i * 1 / n + j * 1 / (2 * n)
                    hy = y + j * (np.sqrt(3)) / (2 * n)
                    hex_pts = self._hexagon(hx, hy, th, scale, hex_type)
                    hex_pts_hom = np.vstack([hex_pts, np.ones(hex_pts.shape[1])])
                    for k in range(ico_triangs.shape[0]):
                        a = ico_triangs[k, 0]
                        b = ico_triangs[k, 1]
                        c = ico_triangs[k, 2]
                        vertices = self._get_projected_face(
                            hex_pts_hom, a, b, c, center=center, radius=radius, ax=ax, plot=plot
                        ).T
                        if create_cells:
                            cell_type = "hexagon" if hex_type == 1 else "half_hexagon"
                            cell = Cell(vertices, cell_type=cell_type)
                            self.cells.append(cell)

        if create_cells:
            self._fix_cells()
            self._add_pentagons()
            self._find_neighbors()

        if plot:
            ax.set_box_aspect([1, 1, 1])
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.set_zlabel("Z")
            plt.tight_layout()
            plt.show()

    def _get_projected_face(
        self, hexagon, u, v, w, center=(0, 0, 0), radius=1, ax=None, plot=False
    ):
        """
        Projects the input face (polygon) onto the unit sphere and optionally plots it.

        Parameters
        ----------
        hexagon : ndarray
            Coordinate array of the planar vertices of the closed shape to be projected,
            shape (3, n) or (4, n).
        u, v, w : int
            Indices (0-based) of the vectors defining the plane to be projected on the sphere.
        center : tuple, optional
            Center of the polyhedron in 3D space (x, y, z). Default is (0, 0, 0).
        ax : matplotlib 3d axis, optional
            If provided, plot on this axis.
        plot : bool, optional
            If True, plot the projected face. Default is False.

        Returns
        -------
        face : ndarray
            Coordinate array of the projected face on the unit sphere, shape (3, n).
        """
        s = 2 / np.sqrt(5)
        c = 1 / np.sqrt(5)
        i = np.arange(5)
        top_points = np.vstack(
            [
                np.zeros(5),
                s * np.cos(i * 2 * np.pi / 5),
                s * np.sin(i * 2 * np.pi / 5),
                c * np.ones(5),
            ]
        ).T
        top_points = np.vstack([[0, 0, 1], top_points[:, 1:]])
        bottom_points = np.column_stack([-top_points[:, 0], top_points[:, 1], -top_points[:, 2]])
        ico_points = np.vstack([top_points, bottom_points])

        n = hexagon.shape[1]
        face = np.zeros((3, n))

        for idx in range(n):
            face[:, idx] = self._map_gridpoint_to_sphere(
                hexagon[:, idx], ico_points[u], ico_points[v], ico_points[w], center=center
            )

        face = face * radius

        if plot:
            if ax is None:
                fig = plt.figure()
                ax = fig.add_subplot(111, projection="3d")
            verts = [face.T]
            color = np.random.rand(
                3,
            )
            poly = Poly3DCollection(verts, alpha=0.3, facecolor=color, edgecolor="none")
            ax.add_collection3d(poly)
            ax.plot(
                face[0, :],
                face[1, :],
                face[2, :],
                "-",
                linewidth=2,
                color="k",
                marker="o",
                markerfacecolor="r",
                markeredgecolor="r",
                markersize=4,
            )
        return face

    def _map_gridpoint_to_sphere(self, p, s1, s2, s3, center=(0, 0, 0)):
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
        """
        l1, l2, l3 = self._barycentric_coords(p)

        if abs(l3 - 1) < 1e-10:
            out = np.asarray(s3)
        else:
            l2s = l2 / (l1 + l2)
            p12 = self._slerp(s1, s2, l2s)
            out = self._slerp(p12, s3, l3)
        return out + center

    def _hexagon(self, x, y, th, scale, hex_type):
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
            Type of hexagon: 1 - full hexagon, 2 - half hexagon.

        Returns
        -------
        hex : ndarray
            2 x N array of hexagon vertices.
        """
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

    def _barycentric_coords(self, p):
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
        """
        x = p[0]
        y = p[1]
        l3 = y * 2 / (3**0.5)
        l2 = x + 0.5 * (1 - l3)
        l1 = 1 - l2 - l3
        return l1, l2, l3

    def _slerp(self, p0, p1, t):
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
        """
        p0 = np.asarray(p0)
        p1 = np.asarray(p1)
        ang0_cos = self._scal_prod(p0, p1) / self._scal_prod(p0, p0)
        ang0_sin = np.sqrt(1 - ang0_cos * ang0_cos)
        ang0 = np.arctan2(ang0_sin, ang0_cos)

        l0 = np.sin((1 - t) * ang0)
        l1 = np.sin(t * ang0)

        out = (l0 * p0 + l1 * p1) / ang0_sin
        return out

    def _scal_prod(self, p1, p2):
        """
        Returns the scalar product of the input vectors p1 and p2.

        Parameters
        ----------
        p1 : array-like
            First vector.
        p2 : array-like
            Second vector.

        Returns
        -------
        out : float
            Scalar product of p1 and p2.
        """
        p1 = np.asarray(p1)
        p2 = np.asarray(p2)
        return np.sum(p1 * p2)

    def _fix_cells(self):
        """
        Fixes cells by merging half hexagonal cells to restore missing vertices.
        """
        # Build a mapping from rounded vertex to half-hexagon cells containing it
        vertex_to_halfhex = {}
        for cell in self.cells:
            if cell.cell_type == "half_hexagon":
                for vertex in [cell.vertices[0], cell.vertices[4]]:
                    key = tuple(np.round(vertex, 4))
                    if key not in vertex_to_halfhex:
                        vertex_to_halfhex[key] = set()
                    vertex_to_halfhex[key].add(cell)

        cells_to_remove = set()
        for cell in self.cells:
            if cell.cell_type != "half_hexagon" or cell in cells_to_remove:
                continue
            # Find candidates sharing both first and last vertex
            shared_cells = vertex_to_halfhex.get(
                tuple(np.round(cell.vertices[0], 4)), set()
            ) & vertex_to_halfhex.get(tuple(np.round(cell.vertices[4], 4)), set())
            shared_cells = [
                c
                for c in shared_cells
                if c is not cell and c.cell_type == "half_hexagon" and c not in cells_to_remove
            ]
            if shared_cells:
                candidate_cell = shared_cells[0]
                # Merge unique vertices from candidate into cell
                for vertex in candidate_cell.vertices:
                    if not np.any(np.all(np.isclose(cell.vertices, vertex, atol=1e-4), axis=1)):
                        cell.vertices = np.vstack((cell.vertices, vertex))
                # Remove the two shared vertices (first and last) to keep only unique ones
                mask = [
                    not (
                        np.all(np.isclose(v, cell.vertices[0], atol=1e-4))
                        or np.all(np.isclose(v, cell.vertices[4], atol=1e-4))
                    )
                    for v in cell.vertices
                ]
                cell.vertices = cell.vertices[mask]
                # Remove duplicates
                _, idx = np.unique(np.round(cell.vertices, 4), axis=0, return_index=True)
                cell.vertices = cell.vertices[np.sort(idx)]
                cell.set_cell_type("hexagon")
                cells_to_remove.add(candidate_cell)
            cell.find_center()
        # Remove merged cells after iteration
        self.cells = [cell for cell in self.cells if cell not in cells_to_remove]

    def _add_pentagons(self):
        """
        Find the missing pentagons and add them to the polyhedron.
        """
        # Count how many times each vertex appears (rounded for stability)
        vertices_count = {}
        for cell in self.cells:
            for vertex in cell.vertices:
                key = tuple(np.round(vertex, 8))
                vertices_count[key] = vertices_count.get(key, 0) + 1

        # Only keep vertices that appear in exactly 2 cells
        pentagon_vertices = [np.array(k) for k, v in vertices_count.items() if v == 2]
        used = set()

        # Build a spatial hash for fast nearest neighbor lookup
        vertex_hash = {tuple(np.round(v, 8)): v for v in pentagon_vertices}

        def find_closest(v, exclude):
            min_dist = float("inf")
            min_key = None
            for key, candidate in vertex_hash.items():
                if key in exclude:
                    continue
                dist = np.linalg.norm(v - candidate)
                if dist < min_dist:
                    min_dist = dist
                    min_key = key
            return min_key

        # Greedily group pentagon vertices by proximity
        while len(used) < len(pentagon_vertices):
            # Find the first unused vertex
            start_key = next(key for key in vertex_hash if key not in used)
            pentagon = [vertex_hash[start_key]]
            used_in_this = {start_key}
            current_key = start_key
            for _ in range(4):
                next_key = find_closest(vertex_hash[current_key], used | used_in_this)
                if next_key is None:
                    break
                pentagon.append(vertex_hash[next_key])
                used_in_this.add(next_key)
                current_key = next_key
            if len(pentagon) == 5:
                self.cells.append(Cell(pentagon, "pentagon"))
            used.update(used_in_this)

    def _find_neighbors(self):
        """
        Finds neighbors for each cell in the Goldberg Polyhedron.
        """
        vertex_to_cells = {}
        for cell in self.cells:
            for vertex in cell.vertices:
                key = tuple(np.round(vertex, 4))
                if key not in vertex_to_cells:
                    vertex_to_cells[key] = set()
                vertex_to_cells[key].add(cell)
            cell.neighbors.clear()

        for cell in self.cells:
            neighbor_cells = set()
            for vertex in cell.vertices:
                key = tuple(np.round(vertex, 4))
                neighbor_cells.update(vertex_to_cells[key])
            neighbor_cells.discard(cell)
            cell.neighbors = neighbor_cells
