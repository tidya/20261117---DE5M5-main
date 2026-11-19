from pathlib import Path
from datetime import datetime

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        self.nirosh = 2.45

    def get_sum(self):
        return self.a + self.b
    
    def get_difference(self):
        return self.a - self.b

    def get_product(self):
        return self.a * self.b

    def get_quotient(self):
        return self.a / self.b
    
    def nirosh_index(self):
        ans = (self.a + self.b)*self.nirosh + 100
        return ans
    
if __name__ == "__main__":
    myCalc = Calculator(a=247,b=12)
    answer = (myCalc.get_quotient())
    print(answer)

out = Path("/data/hello.txt")

with out.open("a") as f:
    f.write(f"{answer}\n")
