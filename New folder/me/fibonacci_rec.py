def fib(n):
	if n==0 or n==1:
		print(n)
		return 1;
	else:
		print(fib(n-1)+fib(n-2))
		
print(fib(int(input("Enter the limit"))))
