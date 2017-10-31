seq = raw_input('what is the source sequence?')
sub_seq = raw_input('what is the sub sequence?')

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
