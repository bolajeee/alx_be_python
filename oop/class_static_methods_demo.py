class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    #Static method to add two numbers.
    def add(a, b):
        return a + b
        
    @classmethod
    #Class method to multiply two numbers.
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b