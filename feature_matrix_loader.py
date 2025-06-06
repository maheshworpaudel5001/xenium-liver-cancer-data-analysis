import zarr
import numpy as np
import scipy.sparse as sparse


class FeatureMatrixLoader:
    def __init__(self, path: str):
        self.path = path
        self.store = self._get_store()
        self.group = zarr.open_group(store=self.store, mode="r")
        self.cell_features = self.group["cell_features"]

    def _get_store(self):
        if self.path.endswith(".zip"):
            return zarr.storage.ZipStore(self.path, mode="r")
        return zarr.storage.LocalStore(self.path)

    def get_attributes(self):
        return dict(self.cell_features.attrs)

    def load_feature_by_cell(
        self, format: str = "csr"
    ) -> sparse.csr_matrix | np.ndarray:
        data = self.cell_features["data"][:]
        indices = self.cell_features["indices"][:]
        indptr = self.cell_features["indptr"][:]
        attrs = self.get_attributes()
        shape = (attrs["number_features"], attrs["number_cells"])

        matrix = sparse.csr_matrix((data, indices, indptr), shape=shape)

        if format == "csr":
            return matrix
        elif format == "2D":
            return matrix.toarray()
        else:
            raise ValueError(f"Unsupported format: {format}. Use 'csr' or '2D'.")

    def load_cell_by_feature(
        self, format: str = "csr"
    ) -> sparse.csr_matrix | np.ndarray:
        matrix = self.load_feature_by_cell(format="csr").T
        if format == "csr":
            return matrix
        elif format == "2D":
            return matrix.toarray()
        else:
            raise ValueError(f"Unsupported format: {format}. Use 'csr' or '2D'.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if isinstance(self.store, zarr.storage.ZipStore):
            self.store.close()