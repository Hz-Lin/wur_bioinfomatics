#!/usr/bin/env python
# fasta2csv script

from sys import argv

FASTA_file = open(argv[1])

ID_line = ""
sequence = ""

for line in FASTA_file:
	line = line.strip()
	
	if line[0] == '>':
		if ID_line != "":
			(identifier,description) = ID_line.split(' ',1)
			print'"%s","%s","%s"'%(identifier,description,sequence)
			ID_line = ""
			sequence = ""
		ID_line = line[1:]
	else:
		sequence += line

if ID_line != "":
	(identifier, description) = ID_line.split(' ', 1)
	print '"%s","%s","%s"' % (identifier, description, sequence)

	FASTA_file.close()
#end script