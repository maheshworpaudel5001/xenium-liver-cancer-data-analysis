import zarr


class ZarrReader:
    def __init__(self, path: str):
        self.path = path
        self.store = self._get_store()
        self.group = zarr.open_group(store=self.store, mode="r")

    def _get_store(self):
        if self.path.endswith(".zip"):
            return zarr.storage.ZipStore(self.path, mode="r")
        return zarr.storage.LocalStore(self.path)

    def get_group(self) -> zarr.Group:
        return self.group

    def __enter__(self):
        return self.group

    def __exit__(self, exc_type, exc_value, traceback):
        if isinstance(self.store, zarr.storage.ZipStore):
            self.store.close()
