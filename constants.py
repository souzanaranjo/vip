from enum import Enum


class Type(Enum):
    ERROR = 0
    INT = 1
    FLOAT = 2
    STRING = 3
    VOID = 4


# Map from string type to Enum type.
types = {
    "int": Type.INT,
    "float": Type.FLOAT,
    "string": Type.STRING,
    "void": Type.VOID
}


class Operator(Enum):
    PLUS = 0
    MINUS = 1
    TIMES = 2
    DIVIDE = 3
    ASSIGN = 4
    GREATER = 5
    LESS = 6
    LESS_EQ = 7
    GREATER_EQ = 8
    EQUALS = 9
    NOT_EQUAL = 10
    AND = 11
    OR = 12
    GOTO = 14
    GOTOF = 15
    PRINT = 16
    READ = 17
    RETURN = 18
    GOSUB = 19
    PARAM = 20
    ERA = 21
    ENDFUNC = 22
    END = 23
    FAKE_BOTTOM = 24
    VER = 25
    POSITIVE_SIGN = 26
    NEGATIVE_SIGN = 27
    NOT = 28


operators = {
    "+": Operator.PLUS,
    "-": Operator.MINUS,
    "*": Operator.TIMES,
    "/": Operator.DIVIDE,
    "=": Operator.ASSIGN,
    ">": Operator.GREATER,
    "<": Operator.LESS,
    "<=": Operator.LESS_EQ,
    ">=": Operator.GREATER_EQ,
    "==": Operator.EQUALS,
    "!=": Operator.NOT_EQUAL,
    "and": Operator.AND,
    "or": Operator.OR,
    "gotof": Operator.GOTOF,
    "goto": Operator.GOTO,
    "(": Operator.FAKE_BOTTOM,
    "not": Operator.NOT
}


class Scope(Enum):
    GLOBAL = 0
    LOCAL = 1
    TEMP = 2


# Map from string scope to Enum scope.
scopes = {
    "global": Scope.GLOBAL,
    "local": Scope.LOCAL,
    "temp": Scope.TEMP,
}

allowed_return_types = [Type.INT, Type.FLOAT, Type.STRING, Type.VOID]
