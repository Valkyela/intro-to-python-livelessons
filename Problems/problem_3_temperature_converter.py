"""
Given a temperature in Fahrenheit, return the temperature in Celsius
"""
# Ask for a temperature in Fahrenheit
temp_f= input("What is the temperature in F:?")
temp_f = int(temp_f)

# Calculate it in Celsius
print(temp_f)

Temp_c = (int(temp_f) - 32) * 5/9
Temp_c = str(Temp_c)

# Tell the user what it is
print("The temperature in C: " + Temp_c)