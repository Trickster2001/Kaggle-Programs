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
