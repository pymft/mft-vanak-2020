str_using_si_units = input("Are you using si units?(Y/N): ")
using_si_units = True
weight_pound = 0.0
weight = 0.0
height_inch = 0.0
height = 0.0
if str_using_si_units == "Y":
    using_si_units = False
    str_using_pound = input("Are you using pound?(Y/N): ")
    using_pound = False
    if str_using_pound == "Y" :
        using_pound = True
        weight_pound = float(input("Please input your weight: "))

    str_using_inch = input("Are you using inch?(Y/N): ")
    using_inc = False
    if str_using_pound == "Y" :
        using_pound = True
        height_inch = float(input("Please input your weight: "))
else:

   weight = float(input("Please input your weight(Kg): "))
   height = float(input("Please input your height(metr): "))
if using_si_units :
    bmi = weight / (height * height)
    print(bmi)
else:
    bmi = weight_pound / (height_inch * height_inch) * 703
    print(bmi)
