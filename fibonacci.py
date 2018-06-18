def fibonacci(n):
if(n<=1):
else:
return(fibonacci(n-1)+fibonacci(n-2))
n=int(input("enter the number of terms:")
print("fibonacci series:")
for i in range(n)
print fibonacci(i)
