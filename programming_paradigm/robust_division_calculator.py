# division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            raise ValueError("Error: Cannot divide by zero.")
        return numerator / denominator
   
    except ValueError as e:
        if denominator != float(denominator):
            return f"Error: Non-numeric denominator '{denominator}'"
        elif numerator != float(numerator):
            return f"Error: Non-numeric numerator '{numerator}'"
        else:
            return f"Error: {str(e)}"
        
