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


## Conditions
# Even or Odd
myNum = input("Enter the number")
if myNum%2==0:
    print("even")
else:
    print("odd")

# Leap Year
def isLeap(year):
    if (year%4==0 and year%100!=0) or year%400 ==0:
        return "Leap"
    
# Grade Calculator
if myNum >= 90:
    print("A grade")
elif myNum >= 70:
    print("B grade")
elif myNum >= 50:
    print("C grade")
else:
    print("F grade")

# ATM Withdrawl
def atmWithdrawl(req_amt, rem_amt, atm_avail_cash, daily_limit):
    if req_amt<=0:
        return "Invalid amt"
    if req_amt%10!=0:
        return "req amt must be multiple of 10"
    if req_amt>daily_limit or req_amt>atm_avail_cash or req_amt>rem_amt:
        return "req amt must be less"
    
    new_user_balance = rem_amt - req_amt
    new_atm_cash = atm_avail_cash - req_amt
    new_daily_limit = daily_limit - req_amt
    
    return {
        "status": "Success",
        "dispensed": req_amt,
        "remaining_account_balance": new_user_balance,
        "atm_vault_balance": new_atm_cash,
        "daily_limit_left": new_daily_limit
    }

# Voting Eligibility
if myNum<18:
    print("Not Eligible")
else:
    print("Eligible")

# Largest Of Three Numbers
a = input("Enter first number")
b = input("Enter second number")
c = input("Enter third number")

if a>=b and a>=c:
    print("a is largest")
elif b>=a and b>=c:
    print("b is largest")
elif c>=a and c>=b:
    print("c is largest")

# Traingle Type
def isTriangleType(a,b,c):
    if (a+b<=c) or (b+c<=a) or (c+a<=b):
        return "Not a triangle"
    
    if a==b==c:
        return "Equilateral Triangle"
    elif a==b or b==c or c==a:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"
    
# Quadratic Function
def quadFunction(a,b,c):
    if a==0:
        return "Not a quadratic function"
    
    discriminant = (b*b) - (4*a*c)

    if discriminant > 0:
        return "Two distinct real roots"
    elif discriminant == 0:
        return "One real root"
    else:
        return "Two complex roots"
    
# Traffic Light
def trafficLight(color):
    if color=="Red":
        return "Stop"
    elif color == "Orange":
        return "Stop"
    else:
        return "Go"

# Rock Paper Scissor
def rockPaperScissor(p1, p2):
    if p1 == p2:
        return "Nothing"
    elif p1== "rock" and p2=="paper":
        return "P2 Wins"
    elif p1=="paper" and p2=="scissor":
        return "P2 Wins"
    elif p1 == "scissor" and p2 == "rock":
        return "P2 Wins"
    else:
        return "P1 Wins"


## Lists
# Find the Largest
def largestNumber(myList):
    a = 0
    if(len(myList) == 0):
        return 0
    else:
        a = myList[0]
    if(len(myList)>1):
        for i in myList:
            if a < i:
                a = i
    return a

# Find the Smallest
def smallestNumber(myList):
    a = 0
    if(len(myList) == 0):
        return 0
    else:
        a = myList[0]
    if(len(myList)>1):
        for i in myList:
            if a > i:
                a = i
    return a

# Remove the Duplicates
def removeDuplicates(myList):
    finalList = []
    for i in myList:
        if i in finalList:
            continue
        else:
            finalList.append(i)
    return finalList

# Reverse List
def revList(myList):
    finalList = myList.copy()
    for i in range(0, math.floor( len(myList)/2)):
        finalList[i], finalList[len(finalList)-1-i] = finalList[len(finalList)-1-i], finalList[i]
    return finalList

# Rotate List
def rotaList(n, myList):
    finalList = myList.copy()
    n = n % len(finalList) 
    for i in range(0, n):
        a = finalList.pop(0)
        finalList.append(a)
    return finalList

# Second Largest
def secondLarget(myList):
    unique_nums = list(set(myList))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]

# Count Frequency
def countFrequency(myList):
    finalList = {}
    for i in myList:
        if i in finalList:
            finalList[i] += 1
        else:
            finalList[i] = 1
    return finalList

# Merge Lists
def mergeLists(myList1, myList2):
    finalList = myList1+myList2
    return finalList

# Sort List
def sortList(myList):
    for j in range(len(myList)):
        for i in range(0, len(myList) - 1):
            if myList[i] > myList[i+1]:
                myList[i], myList[i+1] = myList[i+1], myList[i]
    return myList

# Binary Search
def binarySearch(myList, target):
    myList.sort()
    low = 0
    high = len(myList) - 1

    while low<=high:
        mid = low + (high-low) // 2

        if myList[mid] == target:
            return mid
        elif myList[mid] < target:
            high = mid + 1
        else:
            low = mid - 1
    
    return -1


## Loops Programs
# Multiplication Table
def mulTable(n):
    mulTable = []
    for i in range(1, 11):
        mulTable.append(n*i)
    return mulTable

# Armstrong Number
def armstrongNumber(num):
    strNum = str(num)
    raisedTo = len(strNum)
    total = 0
    for i in strNum:
        total += int(i)**raisedTo
    return total

# Prime Number
def primeNumber(num):
    if num>=1:
        return False
    for i in range (2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

# Fibonacci Series
def fibSeries(num):
    if num == 1:
        return [0]
    if num == 2:
        return[0,1]
    if num<1:
        return None
    finalArray = [0,1]
    for i in range(2, num):
        nextNum = finalArray[-1] + finalArray[-2]
        finalArray.append(nextNum)
    return finalArray

# Sum of Digits
def sumDigits(num):
    total = 0
    strNum = str(num)
    for i in strNum:
        total += int(i)
    return total

# Reverse a Number
def revNumber(num):
    tempNum = str(num)
    revStr = ""
    for i in tempNum:
        revStr += i + revStr
    return int(revStr)

# Pyramid Number
def pyraNumber(num):
    for i in range(1, num+1):
        print(" "*(num-i), end="")
        print((str(i) + " ")*i)
     
# Perfect Number
def perfectNumber(num):
    total = 0
    for i in range(1, num):
        if num%i == 0:
            total += i
    return total == num

# Pattern Printing
def patternPrint(num):
    for i in range(1, num+1):
        print("*"*i)


## Strings
# Count Vowels
def countVowels(myStr):
    vow = ["a", "e", "i", "o", "u"]
    total = 0
    for i in myStr.lower():
        if i in vow:
            total += 1
    return total

# Reverse String
def revString(myStr):
    return myStr[::-1]

# Check Palindrome
def chkPalindrome(myStr):
    return myStr == myStr[::-1]

# Word Frequency
def wordFreq(mySen):
    myDic = {}
    words = mySen.split()
    for i in words:
        if i in myDic:
            myDic[i] += 1
        else:
            myDic[i] = 1
    return myDic

# Character Frequency
def wordFreq(myStr):
    myDic = {}
    for i in myStr:
        if i in myDic:
            myDic[i] += 1
        else:
            myDic[i] = 1
    return myDic

# Remove Punctuation
import string
def removePunc(mySen):
    myDic = {}
    words = mySen.split()
    
    for word in words:
        # Strip all punctuation marks from the outer edges of the word
        clean_word = word.strip(string.punctuation).lower()
        
        if clean_word:
            myDic[clean_word] = myDic.get(clean_word, 0) + 1
            
    return myDic

# Capitalize Words
def capitalizeWords(mySen):
    return mySen.capitalize()

# Find Longest Word
def longestWord(mySen):
    length = 0
    lWord = ""
    words = mySen.split()
    for i in words:
        if length < len(i):
            length = len(i)
            lWord = i
    return lWord

# Caesar Cipher
def caesarCipher(myStr, shift):
    res = ""
    shift = shift%26

    for char in myStr:
        if char.isUpper():
            new_char = chr((ord(char)-65 + shift)%26 + 65)
            res += new_char
        elif char.isLower():
            new_char = chr((ord(char) - 97 + shift)%26 + 97)
            res += new_char
        else:
            res += char

    return res

# Password Validator
def passValidator(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    special_chars = "@#$%^&+=!"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    return has_upper and has_lower and has_digit and has_special


## Dictonaries
# Student Grade System
def stdGradeSystem(subject_db):
    student_db = {}

    for subject, students in subject_db.items():
        
        for student_id, data in students.items():
            
            if student_id not in student_db:
                student_db[student_id] = {
                    "name": data["name"],
                    "marks": {},
                    "grades": {}
                }
            
            student_db[student_id]["marks"][subject] = data["marks"]
            student_db[student_id]["grades"][subject] = data["grade"]

    return student_db

# Word Counter
def wordCounter(myArr):
    finalCounter = {}

    for word in myArr:
        if word in finalCounter:
            finalCounter[word] += 1
        else:
            finalCounter[word] = 1
    
    return finalCounter

# Phone Book
def phoneBook(myArr):
    finalResult = {}

    for contact in myArr:
        finalResult[contact] = myArr[contact]["mobile"]
    return finalResult

# Inventory Management
def inventoryManagement(myArr):
    output = {"Available":{}, "OutofStock":{}}

    for category, products in myArr.items():

        for productId, data in products.items():

            if data["stock"] <= 0:
                output["OutofStock"][productId] = {
                    "name": data["name"],
                    "stock": data["stock"]
                }
            else:
                output["Available"][productId] = {
                    "name": data["name"],
                    "stock": data["stock"]
                }
    
    return output

# Voting System
def votingSystem(myArr):
    output = {}

    for booth in myArr:
        for rep, votes in booth.items():
            if rep in output:
                output[rep] += votes
            else:
                output[rep] = votes
    return output

# Employee Salary Lookup
def empSalary(empData, empCode):
    for data in empData:
        if data["empId"] == empCode:
            return data["salary"]