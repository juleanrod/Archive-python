#first python program! :)
user_last_name = input("What is your last name: ")
user_first_name = input("What is your first name: ")
hourly_wage = int( input ("What is your hourly wage: ") )
number_hours_worked = int( input("How many hours have you worked: ") )
gross_wage = str(number_hours_worked * hourly_wage)
print("Your first name is " + user_first_name)
print("Your last name is " + user_last_name)
print("Your wage is $" + gross_wage)
