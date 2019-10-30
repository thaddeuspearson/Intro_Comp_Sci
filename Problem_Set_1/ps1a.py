#!/usr/bin/env python3

# Helper Functions
def interest(savings):
    return (savings * .04) / 12
    

def House_Hunter():
    print(">>>")
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    # assuming 25% down payment
    down_payment = total_cost * .25
    monthly_savings = (annual_salary / 12) * portion_saved
    total_savings = 0
    num_of_months = 0

    while total_savings < down_payment:
        total_savings += monthly_savings + interest(total_savings)
        num_of_months += 1
    
    print("Number of months: " + str(num_of_months))
    print(">>>")


def main():
    
    print(House_Hunter())

if __name__ == "__main__":
    main()