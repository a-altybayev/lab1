# Strings
# Ex.1

print("Hello")
print('Hello')


# Quotes Inside Quotes
# ex.2
print("It's alright")
print("He is called 'Johnny")
print('He is called "Johnny')


# Assign string to a variable
a = "Hello"
print(a)

# Multiline Strings
a= """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# Strings are Arrays
a= 'Hello worlds!'
print(a[1])


# Looping Through a String
for x in 'banananana':
    print(x)

# String Length
a = "Hello, World"
print(len(a))

# Check String

txt = "The best things in life are free"
print("free" in txt) #'True'
#or
txt = "The best things in life are free"
if 'free' in txt:
    print('yes, "free" is present.')


# Check if NOT

txt = "The best things in life are free"
print("expensive" not in txt)#True
#or 
txt = "The best things in life are free"
if 'expensive' not in txt:
    print("no, 'expensive' is NOT present.")