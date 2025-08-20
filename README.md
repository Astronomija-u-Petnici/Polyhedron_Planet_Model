## Goldberg Polyhedron (`goldberg_polyhedron.py`)

This program makes Goldbergs Polyhedron (Geodesic Sphere of Hex and Pentagons) of given order n.

### `Cell` class

Represents a cell (face) in the Goldberg Polyhedron, which can be a hexagon, pentagon, or half-hexagon. Each `Cell` stores its vertices, type, center, normal vector, and a set of neighboring cells. The class provides methods for rounding and cleaning up vertices, updating the cell type, and finding the geometric center.

### `GoldbergPolyhedron` class

Constructs and manages a Goldberg Polyhedron (a geodesic sphere composed of hexagons and pentagons). This class generates the polyhedron's geometry, creates and manages its `Cell` objects, and provides methods for plotting, fixing cell structures, adding missing pentagons, and finding cell neighbors. The polyhedron is defined by its center, order, and radius.

![Example Output](/goldberg_polyhedron_example.PNG)

## Planet Modeling (`planet.py`)

The `planet.py` module provides classes for modeling a planet using Goldberg polyhedra.

### `Surface` Class

- **Purpose:** Represents a surface patch (cell) on the planet, based on a Goldberg polyhedron cell.
- **Key attributes:**
  - `vertices`: The 3D coordinates of the cell's vertices.
  - `cell_type`: Type of the cell (e.g., 'hexagon', 'pentagon').
  - `temperature`: Temperature value for the surface patch.
  - `normal`: Normal vector of the surface
  - `center`: Center coordinates of the surface
  - `neighbors`: List of neighbor surfaces
- **Usage:** Used to store additional properties (like temperature) for each cell.

### `Planet` Class

- **Purpose:** Represents a planet as a collection of `Surface` objects, inheriting from `GoldbergPolyhedron`.
- **Key attributes:**
  - `center`, `order`, `radius`: Define the geometry of the planet.
  - `surfaces`: List of `Surface` objects covering the planet.
- **Methods:**
  - `save(filename)`: Save the planet object to a file using pickle.
  - `load(filename)`: Load a planet object from a file.
  - `plot()`: Shows an image representation of the planet in a 3D space
  - `integrate()`: Placeholder for time integration of surface properties.

These classes allow you to extend the geometric model with physical properties and simulation capabilities.

-----------------------------------------------------------------------------------
Installing pre-commit
```bash
pip install pre-commit==2.13
pre-commit install
```
