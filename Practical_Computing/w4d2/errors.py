src = open('mydata.txt', 'r')
line = src.read()
src.close()
cols = line.split('\t')
cols.sort()
for element in cols:
    print repr(element)
print line
