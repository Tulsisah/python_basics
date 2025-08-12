#: A program that converts temperatures from Fahrenheit to Celsius 
#and vice versa. 
celcius = int(input("\nEnter temperature in Celsius: "))
fahrenheit = (celcius * 1.8) + 32
print(celcius, "Celsius is equal to", fahrenheit, "Fahrenheit")

fahrenheit2 = int(input("\nEnter temperature in Fahrenheit: "))
celcius2 = (fahrenheit2 - 32) / 1.8  
print(fahrenheit2, "Fahrenheit is equal to", celcius2, "Celsius")
