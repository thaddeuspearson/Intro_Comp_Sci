#!/usr/bin/env python3


# Problem Set Directions:
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/MIT6_0001F16_ps1.pdf


# Helper Functions
def interest(savings):
    return (savings * .04) / 12

def semi_raise(salary, sal_raise):
    return salary + (salary * sal_raise)

def saving_with_raise():
    print(">>>")
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
    # assuming 25% down payment
    down_payment = total_cost * .25
    total_savings = 0
    num_of_months = 0

    while total_savings < down_payment:
        # after every sixth month, get a raise
        if num_of_months % 6 == 0 and num_of_months != 0:
            annual_salary = semi_raise(annual_salary, semi_annual_raise)
        monthly_savings = (annual_salary / 12) * portion_saved
        total_savings += monthly_savings + interest(total_savings)
        num_of_months += 1

    print("Number of months: " + str(num_of_months))
    print(">>>")

def main():
    print(saving_with_raise())

if __name__ == "__main__":
    main()
    