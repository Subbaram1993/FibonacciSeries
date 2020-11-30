
def fib(N):
   if N <= 1 :
     return 1
   else :
     return (fib(N-1) + fib(N-2))

N = int(input("enter the number:\t"))
if N <= 0 :
  print("Enter the positive numbers")
else :
  for i in range(N):
    print(fib(i),end=' ')
print("\nCompleted")
