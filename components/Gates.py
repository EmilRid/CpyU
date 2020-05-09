class Gate:
    def __init__(self, *args):
        if len(args)==1 and type(args[0])==list:
            self.inputs = args[0]
        else:
            self.inputs = list(args)  

class NOT(Gate):
    def __init__(self, input):
        super().__init__(input)
    
    def __call__(self):
        return not self.inputs[0]


class AND(Gate):
    def __call__(self):
        return all(self.inputs)


class OR(Gate):
    def __call__(self):
        return any(self.inputs)

class NAND(Gate):
    def __init__(self, *args):
        super().__init__(*args)
        self.andGate = AND(self.inputs)
        self.notGate = NOT(self.andGate())
        
    def __call__(self):
        return self.notGate()

