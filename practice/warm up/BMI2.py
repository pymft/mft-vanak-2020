imperial_or_standard = input("if you use imperial measurement system, Please type Yes otherwise type No")
print(imperial_or_standard)
if imperial_or_standard == Yes or yes:
    height = input("Please type your height (inch)")
    weight = input("Please type your weight (lbs)")
    weight = float(weight)
    height = float(height)
    bmi = (weight*733) / (height * 100) ** 2
else:
    height = input("Please type your height (cm)")
    weight = input("Please type your weight (kg)")
    weight = float(weight)
    height = float(height)
    bmi = weight / (height * 100) ** 2
#if clause
if bmi <= 18.5:
    print("Underweight")
elif 18.5 < bmi <= 25:
    print("Normal")
elif 25 < bmi <= 30:
    print("Overweight")
else:
    print("Obesity")




