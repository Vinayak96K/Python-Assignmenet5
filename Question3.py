from itertools import *

str1=input("Enter the string:")

print(type(str1))
x=list(permutations(str1))
for str2 in x:
    print(str(str2))