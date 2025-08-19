"""
Module for planet modelling using Goldberg polyhedra.
"""

import pickle

from goldberg_polyhedron import Cell, GoldbergPolyhedron


class Surface(Cell):
    """
    A class representing a surface of a planet using a cell on a Goldberg polyhedra.
    """

    def __init__(self, vertices, cell_type=None, temperature=0):
        """
        Initialize the surface with vertices, cell type, and temperature.

        Parameters:
        - vertices: List of vertices defining the surface.
        - cell_type: Type of the cell (e.g., 'hexagon', 'pentagon').
        - temperature: Temperature of the surface.
        """
        super().__init__(vertices, cell_type)
        self.temperature = temperature

    def __repr__(self):
        """
        Return a string representation of the surface.
        """
        return f"Surface(vertices={self.vertices}, cell_type={self.cell_type}, \
            temperature={self.temperature})"

    @classmethod
    def cell_to_surface(cls, parent):
        """
        Convert a Cell objest to a Surface object.
        """
        return cls(parent.vertices, parent.cell_type)

    def update_temperature(self):
        """
        Update the temperature of the surface.
        """
        pass


class Planet(GoldbergPolyhedron):
    """
    A class representing a planet modelled using Goldberg polyhedra.
    """

    def __init__(self, center=(0, 0, 0), order=2, radius=1):
        """
        Initialize the planet with a center, order of the Goldberg polyhedron, and radius.

        Parameters:
        - center: Center coordinates of the planet.
        - order: Order of the Goldberg polyhedron.
        - radius: Radius of the planet.
        """
        super().__init__(center=center, order=order, radius=radius)
        self.surfaces = [Surface.cell_to_surface(cell) for cell in self.surfaces]

    def __repr__(self):
        """
        Return a string representation of the planet.
        """
        return f"Planet(center={self.center}, order={self.order}, radius={self.radius})"

    @property
    def surfaces(self):
        """
        Returns list of surface cells of the planet.
        """
        return self.cells

    @surfaces.setter
    def surfaces(self, value):
        """
        Set the surfaces (cells) of the planet.

        Parameters:
        - value: List of surface cells to set.
        """
        self.cells = value

    def save(self, filename="planet.pkl"):
        """
        Save the planet's surfaces to a file.

        Parameters:
        - filename: Name of the file to save the planet to.
        """
        pickle.dump(self, open(filename, "wb"))

    @classmethod
    def load(cls, filename):
        """
        Load a PlanetCell object from a file using pickle.

        Parameters:
        - filename: Name of the file to load the planet from.
        """
        with open(filename, "rb") as f:
            obj = pickle.load(f)
            if not isinstance(obj, cls):
                raise TypeError(f"Loaded object is not a {cls.__name__}")
            return obj

    def integrate(self):
        """
        Integrate the planet's surfaces over time.
        """
        pass

    def _integrate_step(self):
        """
        Perform an integration step for the planet's surfaces.
        """
        pass
