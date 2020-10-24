from enum import Enum
class Type(Enum):
     ERROR = 0
     INT = 1
     FLOAT = 2
     STRING = 3
     VOID = 4

# Map from string type to Enum type.
types = {
    "int" : Type.INT,
    "float" : Type.FLOAT,
    "string" : Type.STRING,
    "void" : Type.VOID
}