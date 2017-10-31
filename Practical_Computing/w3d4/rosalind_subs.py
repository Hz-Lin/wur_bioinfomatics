in_file = open('rosalind_subs.txt','r')
out_file = open('rosalind_subs_out.txt','w')

line_num = 0
for line in in_file:
    line = line.strip('\r\n')
    if line_num == 0:
        s = line
    if line_num == 1:
        t = line
    line_num += 1

n = len(t)
locs = []
str_locs = []
for i in range(len(s)-n+1):
    if s[i:i+n] == t:
        locs += [i+1]
for loc in locs:
    loc = str(loc)
    str_locs.append(loc)
out_str = ' '.join(str_locs)
print out_str
out_file.write(out_str)