
#Takings Users Financial Details
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculating Monthly Savings
monthly_savings = monthly_income - monthly_expenses

#Project Annual Savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Output Results
print("Your monthly savings are: $",monthly_savings)
print("Your projected savings after one year, with interest, is: $",projected_savings)
