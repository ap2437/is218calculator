def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
class Calculator:
    result = 0

    def _init_(self):
        pass

    def add(self,a, b):
        self.result=addition(a,b)
        return self.result

    def subtract(self,a,b):
        self.result=subtraction(a,b)
        return self.result

    def multiply(self, a, b):
        self.result=multiply(a,b)
        return self.result

    def divide(self, a, b):
        self.result = divide(a, b)
        return self.result

