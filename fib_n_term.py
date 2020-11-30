def fib(N):
   if N <= 1 :
     return 1
   else :
     return (fib(N-1) + fib(N-2))

N = int(input("enter the term:\t"))
if N < 0 :
  print("Enter the positive numbers")
else :
    print(fib(N-1),end=' ')
print("\nCompleted")
