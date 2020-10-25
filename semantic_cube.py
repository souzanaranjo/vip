#%%
from constants import Type, Operator
semantic_cube = {
    Type.INT: {
        Type.INT:    {
            Operator.PLUS:       Type.INT,
            Operator.MINUS:      Type.INT,
            Operator.TIMES:      Type.INT,
            Operator.DIVIDE:     Type.FLOAT,
            Operator.ASSIGN:     Type.INT,
            Operator.GREATER:    Type.INT,
            Operator.LESS:       Type.INT,
            Operator.LESS_EQ:    Type.INT,
            Operator.GREATER_EQ: Type.INT,
            Operator.EQUALS:   Type.INT,
            Operator.NOT_EQUAL:  Type.INT,
            Operator.AND:        Type.INT,
            Operator.OR:         Type.INT,
        },
        Type.FLOAT: {
            Operator.PLUS:       Type.FLOAT,
            Operator.MINUS:      Type.FLOAT,
            Operator.TIMES:      Type.FLOAT,
            Operator.DIVIDE:     Type.FLOAT,
            Operator.ASSIGN:     Type.INT,
            Operator.GREATER:    Type.INT,
            Operator.LESS:       Type.INT,
            Operator.LESS_EQ:    Type.INT,
            Operator.GREATER_EQ: Type.INT,
            Operator.EQUALS:   Type.INT,
            Operator.NOT_EQUAL:  Type.INT,
            Operator.AND:        Type.INT,
            Operator.OR:         Type.INT,
        },
        Type.STRING: {
            Operator.PLUS:       Type.STRING,
            Operator.MINUS:      Type.ERROR,
            Operator.TIMES:      Type.STRING,
            Operator.DIVIDE:     Type.ERROR,
            Operator.ASSIGN:     Type.ERROR,
            Operator.GREATER:    Type.ERROR,
            Operator.LESS:       Type.ERROR,
            Operator.LESS_EQ:    Type.ERROR,
            Operator.GREATER_EQ: Type.ERROR,
            Operator.EQUALS:   Type.INT,
            Operator.NOT_EQUAL:  Type.INT,
            Operator.AND:        Type.ERROR,
            Operator.OR:         Type.ERROR,
        }
    },
    Type.FLOAT: {
        Type.INT:    {
            Operator.PLUS:       Type.FLOAT,
            Operator.MINUS:      Type.FLOAT,
            Operator.TIMES:      Type.FLOAT,
            Operator.DIVIDE:     Type.FLOAT,
            Operator.ASSIGN:     Type.FLOAT,
            Operator.GREATER:    Type.INT,
            Operator.LESS:       Type.INT,
            Operator.LESS_EQ:    Type.INT,
            Operator.GREATER_EQ: Type.INT,
            Operator.EQUALS:   Type.INT,
            Operator.NOT_EQUAL:  Type.INT,
            Operator.AND:        Type.INT,
            Operator.OR:         Type.INT,
        },
        Type.FLOAT: {
            Operator.PLUS:       Type.FLOAT,
            Operator.MINUS:      Type.FLOAT,
            Operator.TIMES:      Type.FLOAT,
            Operator.DIVIDE:     Type.FLOAT,
            Operator.ASSIGN:     Type.FLOAT,
            Operator.GREATER:    Type.INT,
            Operator.LESS:       Type.INT,
            Operator.LESS_EQ:    Type.INT,
            Operator.GREATER_EQ: Type.INT,
            Operator.EQUALS:   Type.INT,
            Operator.NOT_EQUAL:  Type.INT,
            Operator.AND:        Type.INT,
            Operator.OR:         Type.INT,
        },
        Type.STRING: {
            Operator.PLUS:       Type.STRING,
            Operator.MINUS:      Type.ERROR,
            Operator.TIMES:      Type.ERROR,
            Operator.DIVIDE:     Type.ERROR,
            Operator.ASSIGN:     Type.ERROR,
            Operator.GREATER:    Type.ERROR,
            Operator.LESS:       Type.ERROR,
            Operator.LESS_EQ:    Type.ERROR,
            Operator.GREATER_EQ: Type.ERROR,
            Operator.EQUALS:   Type.INT,
            Operator.NOT_EQUAL:  Type.INT,
            Operator.AND:        Type.ERROR,
            Operator.OR:         Type.ERROR,
        },
    },
    Type.STRING: {
        Type.INT:    {
            Operator.PLUS:       Type.STRING,
            Operator.MINUS:      Type.ERROR,
            Operator.TIMES:      Type.STRING,
            Operator.DIVIDE:     Type.ERROR,
            Operator.ASSIGN:     Type.STRING,
            Operator.GREATER:    Type.ERROR,
            Operator.LESS:       Type.ERROR,
            Operator.LESS_EQ:    Type.ERROR,
            Operator.GREATER_EQ: Type.ERROR,
            Operator.EQUALS:   Type.INT,
            Operator.NOT_EQUAL:  Type.INT,
            Operator.AND:        Type.ERROR,
            Operator.OR:         Type.ERROR,
        },
        Type.FLOAT: {
            Operator.PLUS:       Type.STRING,
            Operator.MINUS:      Type.ERROR,
            Operator.TIMES:      Type.ERROR,
            Operator.DIVIDE:     Type.ERROR,
            Operator.ASSIGN:     Type.STRING,
            Operator.GREATER:    Type.ERROR,
            Operator.LESS:       Type.ERROR,
            Operator.LESS_EQ:    Type.ERROR,
            Operator.GREATER_EQ: Type.ERROR,
            Operator.EQUALS:   Type.INT,
            Operator.NOT_EQUAL:  Type.INT,
            Operator.AND:        Type.ERROR,
            Operator.OR:         Type.ERROR,
        },
        Type.STRING: {
            Operator.PLUS:       Type.STRING,
            Operator.MINUS:      Type.ERROR,
            Operator.TIMES:      Type.ERROR,
            Operator.DIVIDE:     Type.ERROR,
            Operator.ASSIGN:     Type.STRING,
            Operator.GREATER:    Type.INT,
            Operator.LESS:       Type.INT,
            Operator.LESS_EQ:    Type.INT,
            Operator.GREATER_EQ: Type.INT,
            Operator.EQUALS:   Type.INT,
            Operator.NOT_EQUAL:  Type.INT,
            Operator.AND:        Type.INT,
            Operator.OR:         Type.INT,
        },
    },
}
