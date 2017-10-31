import random
p = input('p: ')
n = input('n: ')
num = int(n) + 1
p_flo = float(p)
k = range(0,num)
re_list = []
counts = []
for x in k:
    for y in range(0,x):
        if p_flo > random.random():
            result = 'Y'
            re_list.append(result)
        else:
            result = 'n'
            re_list.append(result)
        count = re_list.count('Y')
        counts.append(count)

for c in k:
    print('%d\t%d' % (c,counts[c]))