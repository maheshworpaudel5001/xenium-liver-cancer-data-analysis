
# 🧬 `cell_stat_loader.py`

## Overview

`cell_stat_loader.py` defines the `SpatialInfo` class, which provides methods to access and manipulate spatial metadata of single cells from a Zarr-formatted dataset. It is typically used in spatial transcriptomics workflows where detailed geometric and summary information per cell is needed — including cell IDs, centroids, areas, and polygon boundaries for cells and nuclei.

---

## 📘 Use Case

This loader is useful when:

- You have Zarr datasets that contain spatial cell annotations.
- You need access to geometric data such as centroids and polygons.
- You want to convert cell IDs into a custom human-readable hex-based format.

---

## 📄 Class: `SpatialInfo`

### Constructor

```python
SpatialInfo(path: str)
```

- **Parameters:**
  - `path` (`str`): Path to a Zarr group or a `.zip` archive containing spatial data.
- **Behavior:**
  - Opens the Zarr group and loads the required arrays:
    - `cell_id`
    - `cell_summary`
    - `polygon_vertices`
    - `polygon_num_vertices`

---

## 🔧 Methods

### `get_cell_id_in_hex(index: int) -> str`

Returns a human-readable hexadecimal-like cell ID.

- Encodes the `prefix` portion of the `cell_id` using a base-16 to a–p mapping.
- Appends the `suffix` to the result.

---

### `get_cell_id_in_int(index: int) -> str`

Returns the raw integer-style ID as `prefix-suffix`.

---

### `get_cell_loc(index: int) -> tuple`

Returns the (x, y) centroid of the **cell**.

---

### `get_nucleus_loc(index: int) -> tuple`

Returns the (x, y) centroid of the **nucleus**.

---

### `get_cell_area(index: int) -> float`

Returns the area of the **cell**.

---

### `get_nucleus_area(index: int) -> float`

Returns the area of the **nucleus**.

---

### `get_cell_polygon(index: int) -> np.ndarray`

Returns the vertex coordinates of the **cell boundary polygon**. The last vertex is a repetition of the first to close the polygon.

---

### `get_nucleus_polygon(index: int) -> np.ndarray`

Returns the vertex coordinates of the **nucleus boundary polygon**. The last vertex is a repetition of the first.

---

### `get_summary(index: int) -> dict`

Returns a summary dictionary of all spatial information for a cell:

```python
{
  'cell_index': index,
  'cell_id_hex': ..., 
  'cell_id_int': ...,
  'cell_centroid': ...,
  'cell_area': ...,
  'cell_polygon': ...,
  'nucleus_centroid': ...,
  'nucleus_area': ...,
  'nucleus_polygon': ...
}
```

---

## 🧠 Internal Helper

### `_convert_cell_id(prefix: int, suffix: int = 1) -> str`

    Encodes a numeric prefix into a unique 8-character hexadecimal string using a shifted alphabet (0 → a, f → p), and appends the suffix.
    | Hex Code     | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | a | b | c | d | e | f |
    |--------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
    | Shifted Code | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p |

For details see Section 'Cell ID format mapping' @ [Overview of Xenium Zarr Output Files](https://www.10xgenomics.com/support/software/xenium-onboard-analysis/1.9/analysis/outputs/xoa-output-zarr)
---

## 📂 Expected Zarr Structure

```
<store>/
├── cell_id               # (N, 2) array: prefix, suffix
├── cell_summary          # (N, 6) array: x, y, area, nucleus_x, nucleus_y, nucleus_area
├── polygon_vertices      # (2, N, V, 2) array for cell/nucleus polygon coordinates
├── polygon_num_vertices  # number of vertices
```

---

## 🧪 Requirements

- `zarr`

Install with:

```bash
pip install zarr
```

---
