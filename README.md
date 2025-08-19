## Goldberg Polyhedron (`goldberg_polyhedron.py`)

This program makes Goldbergs Polyhedron (Geodesic Sphere of Hex and Pentagons) of given order n.

Class Cell represents the hexagon or pentagon cell of the polyhedron.
Class GoldbergPolyhedron creates the polyhedron out of Cell objects.

![Example Output](/goldberg_polyhedron_example.PNG)

## Planet Modeling (`planet.py`)

The `planet.py` module provides classes for modeling a planet using Goldberg polyhedra.

### Surface Class

- **Purpose:** Represents a surface patch (cell) on the planet, based on a Goldberg polyhedron cell.
- **Key attributes:**
  - `vertices`: The 3D coordinates of the cell's vertices.
  - `cell_type`: Type of the cell (e.g., 'hexagon', 'pentagon').
  - `temperature`: Temperature value for the surface patch.
  - `normal`: Normal vector of the surface
  - `center`: center coordinates of the surface
- **Usage:** Used to store additional properties (like temperature) for each cell.

### Planet Class

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
