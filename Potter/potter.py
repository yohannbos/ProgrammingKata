def calcule_prix(series):
	result = 0
	reduction = {0:0, 1: 1, 2: 0.95, 3: 0.90, 4: 0.80, 5: 0.75}
	for tomes in series:
		sub_result = 0
		for tome in range(len(tomes)):
			sub_result += tomes[tome]*8 
		sub_result *=reduction[sum(tomes)]
		result +=sub_result
	return result

class Panier():
	def __init__(self, tomes):
		self.tomes = tomes
	def panier_to_paniers(self):
		series=[]
		old_tomes = self.tomes
		for newtomes in range(max(self.tomes)):
			series.append([])
			for index in range(len(self.tomes)):
				series[newtomes].append(1 if old_tomes[index] >= 1 else 0)
				old_tomes[index] -= 1
		return series