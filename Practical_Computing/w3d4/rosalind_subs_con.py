import sys

len_argv = len(sys.argv)
if len_argv == 1:
    in_file_name = 'rosalind_subs.txt'
    out_file_name = 'rosalind_subs_out.txt'
    sys.stderr.write("used the default filenames\n")
if len_argv == 2:
    in_file_name = sys.argv[2]
    name_list = in_file_name.split('.')
    out_file_name = name_list[0] + '_out.txt'
    sys.stderr.write("the output filename is %s\n" %(out_file_name))
if len_argv == 3:
    in_file_name = sys.argv[2]
    out_file_name = sys.argv[3]

in_file = open(in_file_name,'r')
out_file = open(out_file_name,'w')
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