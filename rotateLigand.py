from rotation_matrix import rotation_matrix as rm
import numpy as np


def rotateLigand(ligand, angle, axis):
	newLigand = np.array([])
	for atom in ligand:
		parts = atom.split()
		if len(parts) == 4:
			x,y,z = float(parts[1]), float(parts[2]), float(parts[3])
			new_coor = np.dot(rm(axis, angle), [x,y,z])
			newLigand  = np.append(newLigand, parts[0]+'    '+str(format(new_coor[0], '.10f'))+'    '+ str(format(new_coor[1], '.10f'))+'    '+ str(format(new_coor[2], '.10f')))
	return newLigand
