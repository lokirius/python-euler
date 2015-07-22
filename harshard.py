from sympy.ntheory import isprime
from sympy import nextprime

def suma_digits(numero):
	suma = 0
	for digit in str(numero):
		suma += int(digit)
	return suma

def harshad(numero):
	xifrat = suma_digits(numero)
	if numero%xifrat == 0:
		return True
	else:
		return False

def strong_harshad(numero):
	xifrat = suma_digits(numero)
	if numero%xifrat != 0:
		return False
	candidat = numero//xifrat
	return isprime(candidat)

def right_harshad(numero):
	while  numero > 0:
		if harshad(numero) == False:
			return False
			break
		numero = numero//10
	else:
		return True


fita = 10**14
primer = 11
suma = 0

while primer < fita:
	candidat = primer//10
	if right_harshad(candidat) == False:
		pass
	elif strong_harshad(candidat) == False:
		pass
	else:
		suma += primer
	primer = nextprime(primer)

print(suma)
