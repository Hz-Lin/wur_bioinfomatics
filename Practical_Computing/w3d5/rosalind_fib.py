n = int(raw_input('n = '))
k = int(raw_input('k = '))
seq = [0, 1, 1]
for i in range(3, n+1):
    seq_i = seq[i-1] + k * seq[i-2]
    # alt: seq_i = seq[-1] + k * seq[-2]
    seq += [seq_i]
print seq[n]
