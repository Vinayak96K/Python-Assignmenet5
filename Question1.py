
def reverse(str1):
    i=0
    j=(len(str1)-1)
    while (i<j):
        temp2=str1[i]
        str1 = str1[:i]+str1[j]+str1[i+1:]
        str1 = str1[:j]+temp2+str1[j+1:]       
        i+=1
        j-=1
    return str1

str2 = input('Enter the string:')
print("String before reverse: {}".format(str2))
print("String after reverse: {}".format(reverse(str2)))