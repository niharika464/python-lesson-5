def rfact(n):
    if n==1:
        return n 
    else:
        return n*rfact(n-1)
    
num=int(input("enter the number:"))

if num<=0:
    print("no factorial exists....")
elif num==0:
    print("the factorial of 0 is 1....")
else:
     print("the factorial is",rfact(num))

 


