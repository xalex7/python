def power(x,n):

	if n==0:
		return 1.0
	half_power = power(x, int(n / 2))

	if n % 2 == 0:
		return half_power * half_power
	else:
		if(n > 0):
				return x * half_power * half_power
		else:
				return (half_power * half_power) / x

# for power (foobar, 1024) there are 12 calls