# String Format
age = 36
txt = "My name is John, I am" + age
print(txt) # TypeError: must be str, not int

# F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt) # My name is John, I am 36

# Placeholders and Modifiers
price = 52
txt = f"The price is {price:.2f} dollars"
print(txt)#The price is 52.00 dollars
#or
txt = f"The price is {20 * 59} dollars"
print(txt)
