def fun():
    iSum=0
    for i in str1:
        iSum+=int(ord(i))
    return float(iSum/len(str1))

str1=input("Enter the string:")
print("Average of ascii value is: {}".format(fun()))