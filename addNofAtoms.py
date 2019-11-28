def addNofAtoms(filename):
	mainfile = open(filename, 'r')
	contents = mainfile.readlines()
	mainfile.close()

	nOfAtoms = len(contents)
	
	contents.insert(0, str(nOfAtoms))
	contents.insert(1, '\n\n')
	contents = "".join(contents)

	mainfile = open(filename, 'w')
	mainfile.write(contents)
	mainfile.close()
