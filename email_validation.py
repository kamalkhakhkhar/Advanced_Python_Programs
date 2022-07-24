import re

def solve(n):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,n):
      return True
   return False

n = input("Enter Email To Check :- ")
print(solve(n))
