#!/usr/bin/env python

"""
Author: Harm Nijveen

Script that finds all orfs in DNA sequences and then prints the peptide sequences
"""

import re
#from sys import argv
argv = ['orf_finder.py', 'input.fa']

def read_fasta(fasta_filename):
	""" reads in sequences from a fasta file 
	Keyword arguments:
        fasta_filename -- name of the fasta file to read
    Returns:
        dictionary with the sequences, keys are the sequences IDs
	"""
	fasta_file = open(fasta_filename)
	
	# the dictionary that will contain the sequences
	sequences = {}
	current_ID = ""
	for line in fasta_file:
		# read the file line by line. Remove the newlines from the end of each line
		line = line.strip()
		
		# if a line starts with a ">" it indicates the start of a new sequence
		if line.startswith(">"):
			# the sequence identifier comes after the ">" character
			current_ID = line[1:]
			
			# create a new dictionary key pointing to an empty sequence
			sequences[current_ID] = ""
		elif current_ID is not "":
			# no identifier line, so it must be a sequence line
			# store the sequence line with the current identifier
			# adding it makes sure we get the full sequence and not just the last line
			sequences[current_ID] += line
			
	return sequences	
	

def transcribe(DNA):
	""" transcribes a DNA sequence to an RNA sequence 
	Keyword arguments:
        DNA -- DNA sequence
    Returns:
        RNA sequence as a string
	"""
	RNA = DNA.replace('T','U')
	return RNA


def reverse_complement(RNA):
	""" creates the reverse complement of an RNA sequence 
	Keyword arguments:
        RNA -- RNA sequence
    Returns:
        the reverse complement of the RNA sequence as a string
	"""
	# reverse the string like we would reverse a list
	reverse = RNA[::-1]
	revc = ''

	# using a dictionary to translate an A to a U, a G to a C, etc.
	compl = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
	for n in reverse:
		revc = revc + compl[n]
		
	return revc 
		
	
	
def find_orfs(RNA):
	""" finds open reading frames in a RNA sequence 
	
	Keyword arguments:
        RNA -- RNA sequence
    Returns:
        a list with strings representing the found open reading frames
	"""

	# rather complicated regex to find orfs. 
	# The "?=" makes sure we find also overlapping orfs
	# findall returns a list with all matches
	matches = re.findall('(?=(AUG([ACGU]{3})*?(UAG|UAA|UGA)))',RNA)
	
	# create an empty list to store the found orfs
	orfs = []
	for match in matches:
		# each match is a list with full and partial matches 
		# the full match is the first element
		orfs.append(match[0])
	return orfs
	
	
def translate(orf):
	""" translates an RNA sequence into a protein sequence 
	
	Keyword arguments:
        orf -- RNA sequence
    Returns:
        the corresponding protein sequence as a string
	"""
	codon_table = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
			  'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
			  'UAU':'Y', 'UAC':'Y', 'UAA':'*', 'UAG':'*',
			  'UGU':'C', 'UGC':'C', 'UGA':'*', 'UGG':'W',
			  'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
			  'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
			  'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
			  'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
			  'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
			  'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
			  'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
			  'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
			  'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
			  'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
			  'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
			  'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}
	
	codon_count = len(orf)/3
	
	prot = ''
	for codon_number in range(codon_count):
		codon_start = codon_number * 3
		codon = orf[codon_start:codon_start+3]
		prot = prot + codon_table.get(codon,'')
		
	# remove the stops at the end
	prot = prot.rstrip("*")
	return prot
	
	
# this is where the main program starts	
if __name__ == "__main__":
	
	# read the file name from the command line
	fasta_filename = argv[1]
	
	# read the sequences from the file into a dictionary 
	sequences = read_fasta(fasta_filename)
	
	# only look at the first sequence in the dictionary
	DNA = sequences.values()[0]
	
	# we need RNA for finding the orfs
	RNA = transcribe(DNA)
	
	# create the reverse complement
	revc = reverse_complement(RNA)

	# find the orfs in both strands (+ and -)
	orfs = find_orfs(RNA)
	orfs += find_orfs(revc)

	# create an empty list to store the found proteins 
	proteins = []
	for orf in orfs:
		# translate each orf to a protein sequence and add it to the list
		protein = translate(orf)
		proteins.append(protein)

	# trick to remove duplicate sequences: turn the list into a set
	proteins = set(proteins)
	
	# trick to convert the list of protein sequences into a single string with newlines
	# between the sequences
	print '\n'.join(proteins)


	
