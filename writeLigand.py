def writeLigand(molecule, ligand):
	mol_file = open(molecule, 'a')
	for i in ligand:
		mol_file.write(i)
		mol_file.write('\n')

	mol_file.close()
