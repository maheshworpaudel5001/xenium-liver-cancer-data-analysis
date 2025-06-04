
# 📦 `feature_matrix_loader.py`

## Overview

`feature_matrix_loader.py` provides the `FeatureMatrixLoader` class, a utility for loading and working with sparse feature matrices stored in [Zarr](https://zarr.readthedocs.io/en/stable/) format. The loader is designed to efficiently handle large feature-by-cell or cell-by-feature matrices, commonly used in spatial transcriptomics or single-cell data analysis.

It supports reading data from both uncompressed Zarr directories and compressed `.zip` archives.

---

## 📘 Use Case

This utility is intended for workflows where:

- A large sparse matrix is saved using Zarr, potentially zipped for portability.
- You need to efficiently load the data in either compressed (`csr_matrix`) or dense (`np.ndarray`) format.
- The data represents either features-by-cells or cells-by-features.

---

## 📄 Class: `FeatureMatrixLoader`

### Constructor

```python
FeatureMatrixLoader(path: str)
```

- **Parameters:**
  - `path` (`str`): Path to a Zarr directory or a zipped Zarr `.zip` file.
- **Behavior:**
  - Opens the Zarr store (directory or zip file).
  - Accesses the `cell_features` group inside the Zarr hierarchy.

---

## 🔧 Methods

### `get_attributes() -> dict`

Returns metadata associated with the `cell_features` dataset.

- **Returns:**
  - `dict`: Attributes from `cell_features.attrs`, e.g., number of features and number of cells.

---

### `load_feature_by_cell(format: str = "csr") -> sparse.csr_matrix | np.ndarray`

Loads the sparse matrix where **rows are features** and **columns are cells**.

- **Parameters:**
  - `format` (`str`, default `"csr"`): `"csr"` returns a SciPy sparse matrix; `"2D"` returns a dense NumPy array.
- **Returns:**
  - `csr_matrix` or `ndarray`: The feature-by-cell matrix.
- **Raises:**
  - `ValueError` if the format is not `"csr"` or `"2D"`.

---

### `load_cell_by_feature(format: str = "csr") -> sparse.csr_matrix | np.ndarray`

Loads the sparse matrix where **rows are cells** and **columns are features**. This is the **transpose** of `load_feature_by_cell()`.

- **Parameters:**
  - `format` (`str`, default `"csr"`): `"csr"` for sparse matrix, `"2D"` for dense matrix.
- **Returns:**
  - `csr_matrix` or `ndarray`: The cell-by-feature matrix.
- **Raises:**
  - `ValueError` if the format is not `"csr"` or `"2D"`.

---

## 🔁 Context Manager Support

The class supports `with` statement usage to ensure proper cleanup when using `.zip` archives.

### `__enter__()` and `__exit__()`

- Automatically closes the `ZipStore` if used.
- Allows usage like:

```python
with FeatureMatrixLoader("cells.zarr.zip") as loader:
    matrix = loader.load_cell_by_feature()
```

---

## 🗂 Example Usage

```python
from feature_matrix_loader import FeatureMatrixLoader

# Load from zipped Zarr
with FeatureMatrixLoader("~/cells.zarr.zip") as loader:
    attrs = loader.get_attributes()
    print("Number of features:", attrs["number_features"])

    feature_by_cell = loader.load_feature_by_cell(format="csr")
    cell_by_feature = loader.load_cell_by_feature(format="2D")
```

---

## 📎 Expected Zarr Structure

The file expects the Zarr group to contain:

```
<store>/
└── cell_features/
    ├── data         # 1D array of non-zero values
    ├── indices      # 1D array of column indices
    ├── indptr       # 1D array of row index pointers
    └── .attrs       # Dictionary with keys: number_features, number_cells
```

These arrays define the CSR (Compressed Sparse Row) representation of the feature matrix.

---

## 🧪 Requirements

- `zarr`
- `numpy`
- `scipy`

Install via:

```bash
pip install zarr numpy scipy
```

---
