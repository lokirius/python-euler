
f = open("matrix.txt","r")
text = f.read().replace(' ','').split('\n')
f.close()

fi = 80
matriu = [0 for _ in range(fi)]
for i in range(fi):
	fila = text[i].split(',')
	matriu[i] = [int(fila[j]) for j in range(fi)]

m = matriu
tamany = fi

b = [[0 for _ in range(tamany)] for _ in range(tamany)]

for i in range(tamany):
	b[i][0] = m[i][0]

for j in range(1, tamany):
	for i in range(tamany):
		b[i][j] = min( [b[k][j-1] + sum( [m[l][j] for l in range(min(k,i), max(k,i) + 1)] ) for k in range(tamany)] )

print(min([b[i][tamany-1] for i in range(tamany)]))
