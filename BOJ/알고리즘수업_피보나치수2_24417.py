import sys
sys.setrecursionlimit(10**7)
class rFibo:
	def __init__(self):
		self.cnt = 0

	def Recursive_Fibonacci(self, number):
		if number == 1 or number == 2:
			return 1
		else:
			self.cnt += 1
			print(self.cnt, number)
			return self.Recursive_Fibonacci(number-1) + self.Recursive_Fibonacci(number-2)

def DP_Fibonacci(number):
	f = [1, 1] + ([0]*number)
	dpcnt = 0
	if number == 1 or number == 2:
		return 1
	else:
		for i in range(3, number):
			dpcnt += 1
			f[i] = f[i-1] + f[i-2]
		else:
			return f[number], dpcnt

if __name__ == "__main__":
	n = 45
	rcnt = rFibo()
	rcnt.Recursive_Fibonacci(n)
	value, dpcnt = DP_Fibonacci(n)
	a, b = ((rcnt.cnt+1)%1000000007), ((dpcnt+1)%1000000007)
	print(a, b)