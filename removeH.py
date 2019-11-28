def removeH(moleculeFileName, ligand, numH):
	molecule = open(moleculeFileName, 'r')

	#finding the atom of the ligand nearest to molecule
	closestAtom = findClosestLigandAtom(ligand)
	parts = closestAtom.split()

	#co-ordinates of the nearest ligand atom
	x,y,z = float(parts[1]), float(parts[2]), float(parts[3])

	
	atoms = molecule.readlines()
	min1, min2, min3 = 100, 100, 100
	closest = [atoms[0], atoms[0], atoms[0]]
#	closest1, closest2, closest3 = atoms[0], atom[0], atom[0]

	for atom in atoms:
		parts = atom.split()
		if parts[0] == 'H':###############
			x1,y1,z1 = float(parts[1]), float(parts[2]), float(parts[3])
			dist = ( (x-x1)**2 + (y-y1)**2 + (z-z1)**2 ) ** 0.5
	
			if dist < min1:
				closest[2] = closest[1]
				closest[1] = closest[0]
				closest[0] = atom
				min3 = min2
				min2 = min1
				min1 = dist
			elif dist < min2:
				closest[2] = closest[1]
				closest[1] = atom
				min3 = min2
				min2 = dist
			elif dist < min3:
				closest[2] = atom
				min3 = dist
	
	for i in range(numH):
		atoms.remove(closest[i])

	molecule.close()

	molecule = open(moleculeFileName, 'w')

	for i in atoms:
		molecule.write(i)



##finds the atom in the ligand which is closest to the molecule
def findClosestLigandAtom(ligand):
	minm = 100
	for atom in ligand:
		parts = atom.split()

		x,y,z = float(parts[1]), float(parts[2]), float(parts[3])
		#length from origin
		length = ( x**2 + y**2 + z**2 ) ** 0.5
		if length < minm :
			closest = atom
			minm = length
	return closest
