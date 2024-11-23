def add(a,b):
   return a+b
  
def subtract(a,b):
    return a-b    

def multiply(a,b):
   return a*b  

def division(a,b):
   try:
      return a/b
   except ZeroDivisionError:
       return float('inf')
   
def modulus(a,b):
    return a%b

def power(a,b):
   return a**b 

def is_greater(a,b):
    return a>b

def is_equal(a,b):
    return a==b

def is_smaller(a,b):
    return a<b
