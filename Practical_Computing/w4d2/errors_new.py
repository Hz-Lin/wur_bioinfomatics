src = open('mydata.txt', 'r')
line = src.read()
src.close()
line = line.split('\n')
header = line[0]
cols = header.split('\t')
cols.sort()
for element in cols:
    print repr(element)
print header