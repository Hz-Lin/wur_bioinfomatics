file_name = 'rosalind_orf.txt'
dna_file = open(file_name, 'r')
dna_seq = ''
line_num = 0
for line in dna_file:
    if line_num > 0:
        line = line.strip('\n')
        dna_seq = dna_seq + str(line)
    line_num += 1
print dna_seq
dna_file.close()
