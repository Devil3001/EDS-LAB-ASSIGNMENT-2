
from datetime import date

def calculate_age(year):
    return date.today().year - year

def rupees_to_dollars(salary):
    return salary / 83   # Approx conversion rate

birth_year = int(input("Enter birth year: "))
salary_rs = float(input("Enter salary in rupees: "))

print("Age:", calculate_age(birth_year))
print("Salary in dollars:", rupees_to_dollars(salary_rs))
