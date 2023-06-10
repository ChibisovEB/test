orbits = [(1,3),(2.5,10),(7,7),(6,6),(4,3)]
elorbits = list(filter(lambda item: item[0] != item[1], orbits))
# elorbits = lambda orbits: orbits * 2
print(orbits)
print(elorbits)