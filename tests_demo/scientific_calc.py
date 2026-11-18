from calculator import Calculator

class SciCalc(Calculator):
    def __init__(self, a, b):
        super().__init__(a, b)

    def get_exp(self):
        return self.a**self.b
    
myCalc = SciCalc(a=2,b=3)
print(myCalc.get_quotient())