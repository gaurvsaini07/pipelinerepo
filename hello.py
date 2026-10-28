##print("Hello World")

# x = 5.7
# print(round(x))


# r=float(input("Enter the radius ="))
# result=(3.14*r**2)
# print("The output is =",round(result,2))

# f=float(input("Temperature of city in F is ="))
# result=(f-32)*5/9
# print(" Temperature in C=",result)


# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("Sum of", num1, "and", num2, "is =", num1 + num2)

# print("Subtraction of", num1, "and", num2, "is =", num1 - num2)

# print("Multiplication of", num1, "and", num2, "is =", num1 * num2)

# print("Division of", num1, "and", num2, "is =", num1 / num2)

# import math
# sqroot=int(input("Enter a num to find sq root"))
# squreroot=sqroot**0.5
# print("square root of" ,sqroot,"is", squreroot)         



# import math

# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))

# s = (a + b + c) / 2

# area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# print("Area of triangle =", area)


# print("""Twinkle, twinkle, little star,
#            How I wonder what you are!
#          Up above the world so high,
#          Like a diamond in the sky.
#            Twinkle, twinkle, little star,
#            How I wonder what you are""")

# print( 'It is  a \"beautiful days\" ')

# s=str("&#39;abc&#39;")
# print(s * 5)

# s= 'a'
# print(ord(s))


# print("'  \"my name is Gaurav Saini\" and 'live in Haridwar', Uttrakhnad' '")

# 'abc'
# print(s * 5)s = 

# print("-" * 50)


# s =str(input("the string is: "))
# print(s.count("a"))

# s = "restart"
# print(s.replace('r', '$',1))

# s = "restart"
# i = s.rfind('r')
# print(s[:i] + '$' + s[i+1:])

# fruits = {'apple', 'banana', 'cherry'}
# fruits.add('orange') 
# print(fruits)

# l=[20,30,40]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)

# color_list = ["Red","Green","White","Black"]
# print(color_list[0])
# print(color_list[3])

# s=str(input("the string is : "))

# if(s[-3:]=="ing"):
#     print(s.replace("ing","ly"))
# else:
#     print(s+"ing")


# Q6: The marks obtained by a student in 5 different Subjects are input through a keyboard. The
# Student gets a division as per the following rules.
# 1. Percentage above or equal to 60 – First Division
# 2. Percentage between 50 and 59 – Second Division
# 3. Percentage between 40 and 49 – Third Division
# 4. Percentage less than 40 – Fail


# Write a python program to Display the result based on the above Criteria.


# marks=float(input("Enter String :"))
# if(marks>=60):
#     print("First Division")
# elif(50<=marks<60):
#      print("Second Division")
# elif(40<=marks<50):
#      print("Third Division")
# elif(marks<40):
#      print("Fail")          


# numbers = [10, 25, 5, 40, 15]

# largest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i

# print("Largest number:", largest)

# numbers = [10, 25, 5, 40, 15]

# smallest = numbers[0]

# for i in numbers:
#     if i < smallest:
#         smallest = i

# print("Smallest number:", smallest)


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest number:", a)
# elif b >= a and b >= c:
#     print("Largest number:", b)
# else:
#     print("Largest number:", c)


# year = int(input("Enter year: "))

# if year % 400 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Not a leap year")
# elif year % 4 == 0:
#     print("Leap year")
# else:
#     print("Not a leap year")

# text = input("Enter a string: ")

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sublist = ["h", "i", "j"]

# list1[2][1][2].extend(sublist)

# print(list1)

list1 = [5, 10, 15, 20, 25, 50, 20]

if 20 in list1:
    index = list1.index(20)
    list1[index] = 200

print(list1)