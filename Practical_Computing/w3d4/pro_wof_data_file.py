#processing the wheel-of-Fortune data file
in_file_name = 'WoFinput.csv'
in_file = open(in_file_name,'r')

#creat a dictionary with names as keys and chances as values
my_dict = {}
line_num = 0
for line in in_file:
    if line_num > 0:
        line = line.strip('\r\n')
        name_chance_list = line.split(',')
        name = name_chance_list[0]
        chance = name_chance_list[1]
        my_dict[name] = float(chance)
    line_num += 1

#sort by names
for key in sorted(my_dict):
    print key

#sort by values
records = my_dict.items()
for name, chance in records:
    print name, chance
    records.sort(key=lambda X:X[1])