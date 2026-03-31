height=float(input("enter your height in cm"))
weight=float(input("enter your weight in kg"))

BMI=weight/(height/100)**2
print(" your BMI is",BMI)

if BMI<=18.4:
    print("underweight")
elif BMI<=24.9:
    print("healthy")
elif BMI<=29.9:
    print("overweight")
elif BMI<=34.9:
    print("severely overweight")
elif BMI<=39.9:
    print("obese")
else:
    print("See a doctor")