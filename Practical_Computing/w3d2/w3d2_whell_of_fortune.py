import random
chances = [100.0, 50.0, 50.0, 75.0, 150.0]
names = ['A','B','C','D','E']
n = input('how many times you want to run? ')
total_num = int(n) + 1
range_list = range(0,total_num)
position = []
for num in range_list:
    rand_n = random.random()
    total_chances = sum(chances)
    distance = total_chances * rand_n
    for chance in chances:
        pos = distance - chance
        if pos > 0 and pos < distance:
            pos_ind = chances.index(chance)
            position.append(pos_ind)
print(position)

counts_list = []
for pos_index in range_list:
    count = position.count(pos_index)
    counts_list.append(count)
print(counts_list)

print('%s\t%s\t%s' % ('student','chance','count'))
for ind in range(len(chances)):
    print('%s\t%1.1f\t%d' % (names[ind],chances[ind],counts_list[ind]))