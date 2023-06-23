class Data:
    def __init__(self):
        self.variables = {}
    
    def read(self, id):
        return self.variables[id]
    
    def read_all(self):
        return self.variables
    
    def write(self, variable, expression):
        variable_name = variable.value
        self.variables[variable_name] = expression