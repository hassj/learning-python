#!/usr/bin/env python3.8

# Gather user information function
def gather_info():
    heigh = float(input("enter your heigh in meters: "))
    weight = float(input("Enter your weight: "))
    system = input("which system you want to use, meter or imperial: ").lower().strip()
    return (heigh, weight, system)

# Body max index formula
"""
Return the body index with given parameter
"""
def cal_bmi(heigh, weight, system = "meter"):
    if system == "meter":
        bmi = (weight/ (heigh **2))
    else:
        bmi = (weight/(heigh **2)) * 703
    return bmi

#main function
while True:
    heigh, weight, system = gather_info()
    if system.startswith('i'):
        bmi = cal_bmi(heigh, weight, system='imperial')
        print(f"Your BMI: {bmi}")
        break
    elif system.startswith('m'):
        bmi = cal_bmi(heigh, weight, system  ='meter')
        print(f"Your BMI: {bmi}")
        break
    else: 
        print("Error: Unknown measure system. Please enter either 'meter' or 'imperial' ")
