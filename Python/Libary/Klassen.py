class Lokaal:
  def __init__(self, naam, richting):
    self.naam = naam
    self.richting = richting

L1 = Lokaal("C1.06", "West")
L2 = Lokaal("C1.04", "West")
L3 = Lokaal("C1.13", "West")

print(L1.naam)
print(L1.richting)
print(L2.naam)
print(L2.richting)
print(L3.naam)
print(L3.richting)