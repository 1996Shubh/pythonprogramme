def fseries(n):
    a=0
    b=1
    c=0
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,end=" ")
        for i in range(n-1):
            a=b
            b=c
            c=a+b
            print(c , end = " ")

num=int(input("enter the number of terms of fibonacci series :"))
fseries(num)
