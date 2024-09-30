def budget():
    # Get user input for monthly income
    monthly_income = float(input("What is your monthly income? "))
    
    # Get user input for percentage of income to save
    savings_percentage = float(input("What percentage of your income do you want to save? "))
    
    # Calculate savings amount
    savings_amount = (savings_percentage / 100) * monthly_income
    
    # Calculate total required spendings (housing and food)
    housing_expense = 700
    food_expense = 50 * 4  # Assuming 4 weeks in a month
    
    total_spending = housing_expense + food_expense
    
    # Calculate remaining budget for spending elsewhere
    remaining_budget = monthly_income - (savings_amount + total_spending)
    
    # Print the results
    print("You can save ${} and spend ${} this month.".format(savings_amount, remaining_budget))

# Call the budget function to start the budgeting process
budget()



