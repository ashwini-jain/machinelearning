# -*- coding: utf-8 -*-
"""pybasic_aryan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XvBBX4OLsTylNiBX1CGrsWZO1dV_ufbh

# Expressions, Operators, Control statements
"""



"""# Operators
- Arithmetic (+, -, *, /, //, %)
- Relational (<, >, <=, >=, !=, ==)
- Shift (>>, <<)
- Assignment (=)
- Logical (and, or, not)
- Bitwise (&, |, !)
- 'in' and 'not in' operator

# << and >>

if n=8 (1000 in binary), n>>1 will give 100 after shifting bits by 1 place to right. 
                         n<<1 will give 10000 after shifting bits by 1 place to left.
"""

n=10
print(n,'binary',format(n,'b'))
print(n,'* 2=',n<<1, format(n<<1,'b'))
print(n,'/ 2=',n>>1,format(n>>1,'b'))

# logical
x = True
y = False
print('x and y is',x and y) # Output: x and y is False
print('x or y is',x or y) # Output: x or y is True
print('not x is',not x) # Output: not x is False

# bitwise
x=10 
y=4
print(x & y) 
print(x | y)
print(x ^ y)

# in and not in

x = 'Hello world'
print('j' in x)    # Output: True
print('h' not in x)   # Output: True

# perform operations on complex numbers

import cmath
a=complex(20+7j)
b=complex(5+3j)
print('a+b',a+b)
print('a-b',a-b)
print('a*b',a*b)
print('a/b',a/b)



"""### Task1 Write a program in python to calculate area of triangle when all three sides are given.
- s=(a+b+c)/2
- area =  √(s(s-a)(s-b)(s-c) )
"""



"""# Control Statements

### Decisions (if-else)

# simple if-else
if(cond):
    stmt
else:
    stmt

# if-else-if
if(cond):
    stmt
elif(cond):
    stmt
    .
    .
    .
else: 
    stmt

# nested if-else
                            if(cond):
                                stmt
                                if(cond):
                                    stmt1
                            else:
                                if(cond):
                                    stmt3
                                else:
                                    stmt4

### Task2: Write a proram that accept a lowercase/uppercase character from the user and check whether the character is a vowel or consonant.
"""

# write your code after this line
str=input('Enter a letter: ')
if(str == 'a' or str == 'e' or str == 'i' or str == 'o' or str == 'u'):
  print(str,'is vowel')
else:
  print(str,'is consonant')

"""### Task3: Write a program to check whether given character is a digit or a character in lowercase or uppercase alphabet. Hint: ASCII value of digit is between 48 to 58 and Lowercase characters in the range of 97 to122, uppercase is between 65 and 90)."""

# write your code after this line
str =

"""### Repetition or loop
- while loop
- for loop

#### While loop

initialization of loop variable
while( condition ):
    stmt 1
    stmt 2
    ...
    update loop variable

##### Task 4: Write a program in Python to print table of any number 'n' provided by user using while loop.
"""

# write your code after this line



"""##### Task 5: Write a program in Python to evaluate the following series using while loop:
    
    1! + 2! + 3! + 4! ...+ n!
hint: use math.factorial(n) function to calculate factorial of number n.
"""



"""##### Task 6: Write a program in Python to enter the numbers till the user wants and at the end it should display the maximum number entered using while loop."""



"""### for loop

for iterable_var_name in range(terminating_value):
    stmt 1
    stmt 2
    ...
    
 for iterable_var_name in range(initial_value,terminating_value):
    stmt 1
    stmt 2
    ...
    
 for iterable_var_name in range(initial_value,terminating_value,updation):
    stmt 1
    stmt 2
    ...
"""

# factorial
n=int(input('Enter a number '))
fact=1
for i in range(n,1,-1):
    fact=fact*i
print(n,'! =',fact)

"""##### Task 7:Write a program in Python to print all numbers from 0 to 9 except 3 and 6 using a for loop."""



"""#### 2 Write a program in Python to get 10 numbers from user using a for loop. The program should print the count of positive numbers, negative numbers and zeroes entered by the user."""

