import unittest
from potter import *

class TestPotter(unittest.TestCase):
	def test_calcule_prix_vide(self):
		self.assertEqual(0, calcule_prix(Panier([0, 0, 0, 0, 0]).panier_to_paniers()))

	def test_calcule_prix_un_livre(self):
		 self.assertEqual(8,calcule_prix(Panier([1,0,0,0,0]).panier_to_paniers()))

	def test_calcule_prix_deux_livre(self):
		 self.assertEqual(2*8*0.95,calcule_prix(Panier([1,1,0,0,0]).panier_to_paniers()))

	def test_calcule_prix_trois_livre(self):
		 self.assertEqual(3*8*0.90,calcule_prix(Panier([1,1,1,0,0]).panier_to_paniers()))

	def test_calcule_prix_trois_livre_2_tomes(self):
		 self.assertEqual(2*8*0.95+8,calcule_prix(Panier([2,1,0,0,0]).panier_to_paniers()))

	def test_calcule_prix_trois_livre_2_tomes(self):
		 self.assertEqual(2*8*0.95+2*8,calcule_prix(Panier([3,1,0,0,0]).panier_to_paniers()))

	def test_calcule_prix_final(self):
		 self.assertEqual(51.20,calcule_prix(Panier([2,2,2,1,1]).panier_to_paniers()))


if __name__ == "__main__":
	unittest.main()

