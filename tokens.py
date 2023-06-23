class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __repr__(self):
        return str(self.value)
    
class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)

class Float(Token):
    def __init__(self, value):
        super().__init__("FLT", value)

class Operation(Token):
    def __init__(self, value):
        super().__init__("OP", value)

class Declaration(Token):
    def __init__(self, value):
        super().__init__("DECL", value)

class Variable(Token):
    def __init__(self, value):
        super().__init__("VAR(?)", value) # Variable name, VAR, data type
        # make a = 5 # VAR(?)

class Boolean(Token):
    def __init__(self, value):
        super().__init__("BOOL", value)
    
class Comparison(Token):
    def __init__(self, value):
        super().__init__("COMP", value)

class Reserved(Token):
    def __init__(self, value):
        super().__init__("RSV", value)