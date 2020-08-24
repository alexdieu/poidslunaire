import sys

def poidslunaire():
	print("Poids actuel ?")
	poids = float(sys.stdin.readline())
	print("Poids pris par année")
	poidsplus = float(sys.stdin.readline())
	print("Nombre d'annés")
	years = float(sys.stdin.readline())
	total = poids + (poidsplus*years)
	poidslune1 = poids*0.165
	poidslune2 = total*0.165
	print("Ton poids dans %s années = %s" % (years, total))
	print("Ton poids sur la lune actuellement est %s et dans %s années , il sera de %s" % (poidslune1, years, poidslune2))
  
poidslunaire()
