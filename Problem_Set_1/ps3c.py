#!/usr/bin/env python3

# Problem Set Directions
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/MIT6_0001F16_ps1.pdf

# Helper Function

def interest(savings):
    return (savings * .04) / 12

def semi_raise(salary):
    return salary + (salary * .07)

def bisectional_search(start, end):
    return (start + end) // 2

def three_year_save(salary, saving_rate):
    savings = 0
    for month in range(1,37):
        monthly_save = (salary / 12) * saving_rate
        savings += interest(savings)
        savings += monthly_save
        if month % 6 == 0:
            salary = semi_raise(salary)
    # print(f"Total savings is: {savings}")   
    return savings

def right_amount():
    print(">>>")
    annual_salary = float(input("Enter the starting salary: "))
    bisectional_search_count = 0
    bi_start = 0
    bi_end = 10000

    while bi_start <= bi_end:
        current_rate = bisectional_search(bi_start, bi_end)
        # print(f"Starting at {bi_start}")
        # print(f"Midpoint is {current_rate}")
        # print(f"Ending at {bi_end}")
        # print()
        bisectional_search_count += 1
        decimal_rate = (current_rate) * .0001
        total_savings = three_year_save(annual_salary, decimal_rate)

        if total_savings < 249900:
            bi_start = current_rate + 1
        elif total_savings > 250100:
            bi_end = current_rate - 1
        else:
            return f"Best savings rate: {decimal_rate}\nSteps in bisection search: {bisectional_search_count}\n>>>"
    
    return "It is not possible to pay the down payment in three years.\n>>>"  
        
    



def main():
    print(right_amount())

if __name__ == "__main__":
    main()