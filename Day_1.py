Que-1:
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True

Code:
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
    
    
  ####################################################
  
  Que-2:
  We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
  We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False

Code : 
def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or (not a_smile and not b_smile):
    return True
  else:
    return False
    
    
Que-3: 
Given two int values, return their sum. Unless the two values are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8 
    
Code:
def sum_double(a, b):
  if a!=b:
    return a+b
  else:
    return 2*(2*a)    
  
  
  Que-4: 
  Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
  
 Ans: 
 def diff21(n):
  if n < 21:
    return abs(21-n)
  elif n==21:
    return 0
  else:
    return 2*abs(21-n)
    
    Que-5: 
    We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
    We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
    
Code :
def parrot_trouble(talking, hour):
  if talking and (hour <7 or hour > 20):
    return True
  else:
    return False
   
   
   Que-6 : 
   Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True


Code:
def makes10(a, b):
  if a+b == 10 or a ==10 or b==10 :
    return True
  else:
    return False    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
