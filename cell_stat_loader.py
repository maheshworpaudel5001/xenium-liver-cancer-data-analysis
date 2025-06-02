import zarr

class SpatialInfo:
    def __init__(self, path: str):
        self.path = path
        self.store = self._get_store()
        self.group = zarr.open_group(store=self.store, mode="r")
        self.cell_id = self.group["cell_id"][:]
        self.cell_summary = self.group["cell_summary"][:]
        self.polygon_num_vertices = self.group["polygon_num_vertices"][:]
        self.polygon_vertices = self.group["polygon_vertices"][:]
    
    def _get_store(self):
        if self.path.endswith(".zip"):
            return zarr.storage.ZipStore(self.path, mode="r")
        return zarr.storage.LocalStore(self.path)    
    
    def get_cell_id_in_hex(self, index:int):
        return self._convert_cell_id(prefix=self.cell_id[index][0], suffix=self.cell_id[index][1])
    
    def get_cell_id_in_int(self, index:int):
        return f'{self.cell_id[index][0]}-{self.cell_id[index][1]}'
    
    def get_cell_loc(self, index:int):
        return (self.cell_summary[index][:2])
    
    def get_nucleus_loc(self, index:int):
        return (self.cell_summary[index][3:5])
    
    def get_cell_area(self, index:int):
        return (self.cell_summary[index][2])
    
    def get_nucleus_area(self, index:int):
        return (self.cell_summary[index][5])
    
    def get_cell_polygon(self, index:int):
        """
            # returns vertices in order x1, y1, x2, y2.....
            # last vertex is the first vertex repeated.
        """
        return self.polygon_vertices[1][index]
    
    def get_nucleus_polygon(self, index:int):
        """
            # returns vertices in order x1, y1, x2, y2.....
            # last vertex is the first vertex repeated.
        """
        return self.polygon_vertices[0][index]
    
    def get_summary(self, index:int):
        return {'cell_index':index,
                'cell_id_hex':self.get_cell_id_in_hex(index), 
                'cell_id_int':self.get_cell_id_in_int(index),
                'cell_centroid':self.get_cell_loc(index),
                'cell_area':self.get_cell_area(index),
                'cell_polygon':self.get_cell_polygon(index),
                'nucleus_centroid':self.get_nucleus_loc(index),
                'nucleus_area':self.get_nucleus_area(index),
                'nucleus_polygon':self.get_nucleus_polygon(index)}
    
    ##############################################################
    ##############################################################
    ###################### HELPER FUNCTIONS ######################
    ##############################################################
    
    def _convert_cell_id(self, prefix: int, suffix=1):
        # Step 0: Convert to hex and strip the '0x' prefix
        hex_str = hex(prefix)[2:]

        # Step 1: Pad to 8-digit hex string
        padded_hex = hex_str.zfill(8).lower()

        # Step 2: Create mapping from hex to shifted range
        hex_chars = "0123456789abcdef"
        shifted_chars = "abcdefghijklmnop"
        hex_to_shifted = {h: s for h, s in zip(hex_chars, shifted_chars)}

        # Step 3: Apply character mapping
        shifted = "".join(hex_to_shifted[char] for char in padded_hex)

        # Step 4: Append dataset_suffix
        return shifted + f"-{suffix}"