from constants import Type

# TODO: Consider deleting this class. I'm not sure if the new implementation of var makes this useless.

class Operand:

    def __init__(self, str_operand=None, op_type=None, address=None, is_assigned=False, is_array=False):
        self.str_operand = str_operand

        self.type = op_type

        self.address = address

        self.is_array = is_array

        self.is_assigned = is_assigned

    def __repr__(self):
        return f"Operand({self.str_operand}, {self.type}, {self.address})"

    def set_str_operand(self, str_operand):
        self.str_operand = str_operand

    def get_str_operand(self):
        return self.str_operand

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_dims(self, dims):
        self.dims = dims

    def append_dim(self, dim):
        self.dims.append(dim)

    def get_dims(self):
        return self.dims

    def set_is_assigned(self, is_assigned):
        self.is_assigned = is_assigned

    def get_is_assigned(self):
        return self.is_assigned
