#Global Variables

x= 'awesome'

def myfunc():
    print("python is "+ x)

myfunc()
#output: python is awesome


x='awesome'
def myfunc():
    x = 'fantastic'
    print("Python is " +x)
myfunc()
print("python is "+ x)
#Output:
#Python is fantastic
#python is awesome


#The global Keyword
#Ex 1
def myfunc():
    global x
    x= "fantastic"
myfunc()
print("Py is " + x)
#Output: Py is fantastic

#Ex 2
x= 'awesome'
def myfunc():
    global x
    x= 'fantastic'
myfunc()
print("Python is " +x)
#Output: Python is fantastic