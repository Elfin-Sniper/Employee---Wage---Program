                                                                                  
import random

def check_attendance():
    print ("Welcome to Employee Wages Computation Program on Master Branch")
    attendance = random.choice([1, 0])
    return attendance


def emp_daily_wage(): 
    wage_per_hr = 20 
    emp_check = check_attendance()

    if emp_check == 1:
        daily_wage = wage_per_hr * 8
        print (f"The Employee is present for full day so the daily Wage is: {daily_wage}")
    else:  
        daily_wage = 0
        print(f"Employee is absent for the day is:{daily_wage}")


if __name__ == "__main__":
    emp_daily_wage()
