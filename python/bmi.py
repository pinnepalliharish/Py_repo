

height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))


BMI=weight/(height)**2

if BMI<=18.5:
  print(f"your BMI value is : {round (BMI)} ,your are underweight")    
elif BMI<=25:
  print(f"your BMI value is :{round(BMI)},you have a normal weight")
elif BMI<=30:
  print(f"your BMI value is :{round(BMI)},you are slightly over weight ")
elif BMI<=35:
  print(f"your BMI value is :{round(BMI)},you are obesed")
else:
  print(f" your BMI value is : {round(BMI)},ur clinically obesed")






