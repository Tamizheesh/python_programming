x=10
y=-440
z=127e5
a=3+5j

print("The value of X is  : ",x," The type of x is : ",type(x))
print("The value of y is : ",y,"   The type of y is: ",type(y))
print("The value of z is : ",z, "  The type of z is : ",type(z)) 
print("The value of a is : ",a," The type of a is : ",type(a))

print()
# Type convertion
#covert from int to float
print("The value of float for int x is : ",float(x))

#convert from float to int
print("The value of int for float z is : ",int(z))

#Convert from int to complex
print("The value of complex to int x is :",complex(x))

#Random numbers
print()
print()
import random
print("The Random number between 1 and 10 is :" ,random.randrange(1,10))

