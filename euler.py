# test de primaritat simple.
def primer(p):
	p = abs(p)
	if p == 1:
		return False
	arrel = int(p**0.5)+1
	for i in range(2,arrel):
		if p%i == 0:
			return False
	return True

def factor(n):
	arrel = int(n**0.5) + 1
	fact = []
	i = 2
	while i < arrel:
		if not(primer(i)):
			i += 1
		elif n%i == 0:
			fact.append(i)
			n = n//i
		else:
			i += 1
	if n != 1:
		fact.append(n)
	return fact
