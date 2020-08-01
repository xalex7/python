def digit_sum(n):

		if n<10:
				return n
		else:
				return digit_sum(int(n/10))+ n%10
