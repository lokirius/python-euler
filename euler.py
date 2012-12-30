# test de primaritat simple.
def isprime(p):
	p = abs(p)
	if p == 1:
		return False
	arrel = int(n**0.5)+1
	for i in range(2,arrel):
		if p%i == 0:
			return False
	return True
