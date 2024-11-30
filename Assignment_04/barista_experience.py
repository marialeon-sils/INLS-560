# Assignment 4

# Constants for barista job requirements
MIN_YEARS_COFFEE_EXPERIENCE = 3
MIN_CUSTOMER_SERVICE_EXPERIENCE = 2

# User input1
years_coffee_experience = int(input("Enter your years of experience with coffee: "))
years_customer_service_experience = int(input("Enter your years of customer service experience: "))

if years_coffee_experience >= MIN_YEARS_COFFEE_EXPERIENCE and years_customer_service_experience >= MIN_CUSTOMER_SERVICE_EXPERIENCE:
    print("Congratulations! You meet the requirements to be hired as a barista.")
else:
    print(f'''
Sorry, you do not meet the requirements to be hired as a barista.

You need at least:
- {MIN_YEARS_COFFEE_EXPERIENCE} years of coffee experience
- {MIN_CUSTOMER_SERVICE_EXPERIENCE} year(s) of customer service experience
''')
