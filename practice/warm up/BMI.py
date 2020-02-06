height = input("Please type your height (cm)")
weight = input("Please type your weight (kg)")
weight = float(weight)
height = float(height)
bmi = weight/(height*100)**2
if bmi <= 18.5:
    print("Underweight")
elif 18.5 < bmi <= 25:
    print("Normal")
elif 25 < bmi <= 30:
    print("Overweight")
else:
    print("Obesity")

