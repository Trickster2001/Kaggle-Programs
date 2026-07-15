## Arithmetic and Variables
# Temperature Converter
def tempConvert(temp):
    return (temp*1.8) + 32

# BMI Calculator (weight in kg and height in meter)
def bmiCalculator(bdWeight, bdHeight):
    return bdWeight/(bdWeight*bdHeight)

# EMI Calculator
def emiCalculator(amount, rate, duration):
    return ((amount*rate)*(1+rate)^duration)/(1+rate)^duration - 1

# GST Calculator
def gstCalculator(amount, percent):
    return (amount*percent)/100

# Compound Interest Calculator
def ciCalculator(amount, rate, n, t):
    return amount*((1 + rate/n)^(n*t))

# Age Calculator
from datetime import date
def ageCalculator(birthDate):
    current = date.today()
    return current.year - birthDate.year - ((current.month, current.day) < (birthDate.month, birthDate.day))

# Currency Converter
# dollar to rupees
def currencyConverter(amount):
    return amount*96.25

# Speed, Distance, time Formula
def sdtFormula(speed, distance, time):
    speedReal = distance/time
    distanceReal = speed*time
    timeReal = distance/speed
    return speedReal, distanceReal, timeReal

# Percentage Calculator
def percentCalculator(percent, full):
    return (percent/100)*full


## Functions
# Factorial
def factorial(num):
    if num<0:
        return 0
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)
def factorial1(num):
    if num<0:
        return 0
    if num==0 or num==1:
        return 1
    total = 1
    for i in (2, num):
        total *= i
    return total

# Prime
import math
def myPrime(n):
    if n<=1: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def prime(n):
    count = 0
    myList = []
    for i in range(2, n):
        if(myPrime(i)):
            myList.append(i)
            count += 1
        if count == n:
            break
    return myList

# Fibonacci
def Fibonacci(n):
    if n==1:
        myFibList = [0]
    if n==2:
        myFibList = [0,1]
    n1, n2 = 0,1
    myFibList = [0,1]
    for i in range(3, n+1):
        n3 = n1+n2
        myFibList.append(n3)
        n1=n2
        n2=n3
        
    return myFibList

# Palindrome
def Palindrome(n):
    n = str(n)
    temp = n
    n = n[::-1]
    if temp == n:
        return True
    else:
        return False

# GCD Calculator
def gcdCalculator(a, b):
    while b:
        a,b = b, a%b
    return a

# LCM Calculator
def lcmCalculator(a,b):
    if a==0 or b==0:
        return 0
    return abs(a//gcdCalculator(a,b))*b

# Discount Calculator
def discountCalculator(oPrice, dPercent):
    return oPrice*(dPercent/100)

# Tax Calculator
def taxCalculator(oPrice, tPercent):
    return oPrice*(tPercent/100)

# Max Calculator
def maxCalculator(myArr):
    if not myArr:
        return None
    return max(myArr)

# Average Marks Calculator
def averageMarksCalculator(myArr):
    if not myArr:
        return 0.0
    return sum(myArr) / len(myArr)