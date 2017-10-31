infile = open('rosalind_subs.txt', 'Ur')
outfile = open ('answer_subs.txt', 'w')

line_num = 0
for line in infile:
	line = line.strip('\n')
	if line_num == 0:
		seq = line
	if line_num == 1:
		sub_seq = line
	line_num += 1

pos_list = []
length = len(seq)
length_sub = len(sub_seq)

for start_point in range(length - length_sub):
    end_point = start_point + length_sub
    small_seq = seq[start_point:end_point]
    if small_seq == sub_seq:
        pos = start_point + 1
        pos_str = str(pos)
        pos_list.append(pos_str)
positions = ' '.join(pos_list)

print positions
outfile.write(positions)

infile.close()
outfile.close()