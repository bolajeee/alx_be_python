# This script calculates the users total monthly savings and potential future savings
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05 )

print(f"Your total monthly savings is: {monthly_savings}")
print(f"Your projected savings after one year is: {projected_savings}")
