
import numpy as np
import math

from rotation_matrix import rotation_matrix as rot 
from rotateLigand import rotateLigand
from writeLigand import writeLigand
from removeH import removeH
from shutil import copyfile

#A function that formats data with 10 decimal digits after decimal points 
float_formatter = lambda value: '.10f' % value

#So that everything after this prints in %.10f format, even arrays
np.set_printoptions(formatter={'float_kind':float_formatter})


molecule = 'molecule.xyz'
final_molecule = 'outmol.xyz'
radius = 5.8 #radius of molecule
bondlength = 1.41 
numH = 1 #number of Hydrogens to be removed from the CND that is nearest to the ligand


#copying intial molecule co-ordinates to a new file- final_molecule.
copyfile(molecule, final_molecule)

ligand = open('lig.xyz', 'r')

#print ligand.readlines()


xaxis = [1,0,0]
yaxis = [0,1,0]
zaxis = [0,0,1]
axis4 = [1,1,1]
axis5 = [-1,1,1]
axis6 = [-1,-1,1]
axis7 = [-1,1,-1]
axis8 = [-1,-1,-1]



#an empty list to store all the ligands
ligands = []

#Creating coordinates of first ligand on the x-axis
ligand1 = np.array([])
dist = (radius + bondlength) -  0.25
for line in ligand.readlines():
	#break each line into individual data 
	parts = line.split()
	if len(parts) == 4:	
		x,y,z = float(parts[1]) + dist, float(parts[2]) , float(parts[3])
		ligand1 = np.append(ligand1, parts[0]+'    '+str(format(x,'.10f'))+'    '+str(format(y,'.10f'))+'    '+str(format(z,'.10f')))

ligands.append(ligand1)
#print ligand1
#for i in ligand1:
#	molecule.write(i)
#	molecule.write('\n')
#	print i	

removeH(final_molecule, ligand1, numH)


##################################################################




#rotate the added ligand around one of the eight axes by a specific angle
angle = math.pi #90 degrees

#
ligand2 = rotateLigand(ligand1, angle, zaxis) ##ligand1 passed as an array
removeH(final_molecule, ligand2, numH)
ligands.append(ligand2)

#ligand3 = rotateLigand(ligand2, math.pi/2, zaxis)
#removeH(final_molecule, ligand3, numH)
#ligands.append(ligand3)
#
#ligand4 = rotateLigand(ligand3, math.pi/2, zaxis)
#removeH(final_molecule, ligand4, numH)
#ligands.append(ligand4)
#
#ligand5 = rotateLigand(ligand1, math.pi/2, yaxis)
#removeH(final_molecule, ligand5, numH)
#ligands.append(ligand5)
#
#ligand6 = rotateLigand(ligand1, -1*math.pi/2, yaxis)
#removeH(final_molecule, ligand6, numH)
#ligands.append(ligand6)
#
##print ligand2
for lig in ligands:
	writeLigand(final_molecule, lig)


from addNofAtoms import addNofAtoms
#Add the number of atoms at the beginning so that the file is readable by avogadro/jmol
addNofAtoms(final_molecule)
