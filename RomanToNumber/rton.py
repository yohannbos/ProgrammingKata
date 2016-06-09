def converti(roman):
	dico = {"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000
		}
	somme = 0
	old = 0
	for letter in roman[::-1]:
		if dico[letter] < old:
			somme -= dico[letter]
		else:
			somme += dico[letter]
		old = dico[letter]
	return somme
