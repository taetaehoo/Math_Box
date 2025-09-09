#기본 계산기

def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide_new(a, b):
	return a / b

def get_Median(a, b):
	return (a + b) / 2

def get_Remainder(a, b):
	return a // b

def get_abs(a):
	if num >= 0:
		return num
	else:
		return num * -1
	
def get_Percent(a, b):
	return (a / b) % 100

def get_Sum_ver1(n):
	return n * (n + 1) / 2

def factorial(n):
	
	sum = 1

	for i in range(1, n+1):
		sum *= i

	return sum