def reverse(a):
    return a[::-1]

def is_palindrome(s):
    result=".join(char.lower()for char in s)"
    return result==result[::-1]

def count_vowels(s):
   vowels="aeiouAEIOU"
   count=0
   for char in s:
       if char in vowels:
           count+=1
           return count

def upper_case(a):
      b=a.upper()
      return b

def capitalize(a):
   return a.capitalize()
    
def update_string(s,old,new):
    return s.replace(old,new)
    
def find_substring(s,target):
    return s.find(target)
  

def split_string(s,sp):
    return s.split(sp)
   

def joint_string(s,delimiter):
   return delimiter.join(s)