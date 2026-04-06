def convert(fahrenheit):
  celsius= (fahrenheit - 32) * 5/9
  return celsius
fahrenheit_input= float(input("Enter the temperature in Fahrenheit:"))
celsius_value= convert(fahrenheit_input)
print(f"{fahrenheit_input} Fahrenheit is equal to {celsius_value:.2f} Celsius")
if celsius_value > 20:
  print("IT'S HOT HERE")
else:
  print("IT'S COLD HERE")
 
