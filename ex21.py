# -*- coding: utf-8 -*-

def add(a, b):
	print("ADDING %d + %d" % (a, b))
	return a + b
	
def subtract(a, b):
	print("SUBTRACTING %d - %d" % (a, b))
	return a - b
	
def multiply(a, b):
	print("MULTIPLYING %d * %d" % (a, b))
	return a * b
	
def divide(a, b):
	print("DIVIDING %d / %d" % (a, b))
	return a / b
	
def square(a):
	print("SQUARING %d ^ 2" % a)
	return a * a
	
print("Let's do some math with just functions!")

age = add(22, 3)
height = subtract(55, 7)
weight = multiply(100,4)
iq = divide(200, 20)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

print(square(4))