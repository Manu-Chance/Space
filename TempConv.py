#! python3


def celsius_to_fahrenheit(celsius):
#	print(f"Celsius: {celsius}")
	fahrenheit = (celsius * (9 / 5)) + 32
	return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
#	print(f"Fahrenheit: {fahrenheit}")
	celsius = (fahrenheit - 32) * (5 / 9)
	return celsius

def celsius_to_kelvin(celsius):
#	print(f"Celsius: {celsius}")
	kelvin = (celsius + 273.15)
	return kelvin

def fahrenheit_to_kelvin(fahrenheit):
#	print(f"Fahrenheit {fahrenheit}")
	kelvin = (fahrenheit - 32) * (5 / 9) + 273.15
	return kelvin

def kelvin_to_celsius(kelvin):
#	print(f"Kelvin: {kelvin}")
	celsius = (kelvin - 273.15)
	return celsius

def kelvin_to_fahrenheit(kelvin):
#	print(f"Kelvin: {kelvin}")
	fahrenheit = ((kelvin - 273.15) * (9 / 5) + 32)
	return fahrenheit


'''
print(f"Fahrenheit: {celsius_to_fahrenheit(0)}")	# Result = 32
print(f"Celsius: {fahrenheit_to_celsius(0)}")		# Result = -17.7778
print(f"Kelvin: {celsius_to_kelvin(0)}")		# Result = 273.15
print(f"Kelvin: {fahrenheit_to_kelvin(0)}")		# Result = 255.372
print(f"Celsius: {kelvin_to_celsius(0)}")		# Result = -273.15
print(f"Fahrenheit: {kelvin_to_fahrenheit(0)}") 	# Result = -459.67
'''
