#Step 2 Welcoming message
print("Welcome to the Income Calculator!\n")
print("This program calculates an employee's gross income, income tax deduction, superannuation deduction, and net income based on the hours worked and the provided hourly rate.")

#Step 2.1 Create the program's main loop
while True:

    # Step 3 Obtain user's input (employee's name)
    employee_name = input('\n'+"Enter the employee's name:" + '\t')

    # Step 4 Part of the data validation process for the hours worked
    while True:
        # Step 4.1 Obtain user's input (hours worked) and covert it to variable type float
        hours_worked = float(input("Enter the hours worked:" + '\t'))

        # Step 4.2 Validate user input
        if hours_worked < 0:
            print('\n'+"The number of hours worked must be greater than 0.")

        # Step 4.3 Break the data validation loop for the hours worked
        else:
            break

    # Step 5 Part of the data validation process for the hourly rate
    while True:
        # Step 5.1 Obtain user's input (hourly rate) and covert it to variable type float
        hourly_rate = float(input("Enter the hourly rate:" + '\t'))

        # Step 5.2 Validate user's input
        if hourly_rate < 0:
            print('\n'+"The hourly rate must be greater than 0.")

        # Step 5.3 Break the data validation loop for the hourly rate
        else:
            break

    # Step 6 Calculate Gross Income (GI)
    gross_income = hours_worked * hourly_rate

    # Step 7 Calculate Income Tax Deduction (TD)
    income_tax_deduc = gross_income * 0.2

    # Step 8 Calculate Superannuation Deduction (SD)
    super_deduc = gross_income * 0.1

    # Step 9 Calculate Net Income (NI)
    net_income = gross_income - income_tax_deduc - super_deduc

    # Step 10 Print Employee's name
    print('\n'+ "Results:" + '\n' + "Employee’s Name: " + employee_name)

    # Step 11 Print Gross Income
    print("Gross Income: $" + str(gross_income))

    # Step 12 Print Income Tax Deduction
    print("Income Tax Deduction: $" + str(income_tax_deduc))

    # Step 13 Print Superannuation Deduction
    print("Superannuation Deduction: $" + str(super_deduc))

    # Step 14 Print Net Income
    print("Net Income: $" + str(net_income))

    # Step 15 Ask the user if they want to keep the loop
    print('\n'+"Would you like to calculate another employee's income?")

    # Step 16 Obtain user's input (Decision to keep the loop)
    decision=input("Type 'Yes' or 'No':"+'\t')

    # Step 16.a Decision is "Yes"
    if decision.lower() == "yes":
        pass

    # Step 16.b Decision is "No"
    else:
        print('\n' + "Thank you for using the Income Calculator program.")
        # Step 16.b.1 This function will break the loop
        break