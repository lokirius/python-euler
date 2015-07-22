from sympy import primerange, sieve

def sumar(suma,primer):
	suma += primers[primer]
	if suma > limit:
		return False
	quants[suma] += 1
	while sumar(suma,primer) == True:
		primer += 1
		if primer == ultim:
			return False
	return True

def comptar(limit):
	primers = list(sieve.primerange(1,limit))
	ultim = len(primers)

	quants = [0 for _ in range(limit+1)]
	for i in range(ultim):
		a = sumar(0,i)

	for i in range(2,limit+1):
		if quants[i] > 5000:
			return i

print(comptar(100))
