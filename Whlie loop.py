# Factorial
n = int(input('enter a number for factorial: '))
s=1
while n>0:
    s = s * n
    n= n -1
print(s)

# Fibonacci series
i = int(input('enter a number for fibonacci series: '))
n=0
a=0
print(a)
b=1
while n<=i:
    n=n+1
    print(b)
    c=a+b
    a=b
    b=c