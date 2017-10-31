#open the input and output files
in_file_name = 'some_crane_data.xml'
out_file_name = 'some_crane_data.csv'
in_file = open(in_file_name,'r')
out_file = open(out_file_name, 'w')

import re

#creat a set of column names
columns = set()
search_str = r"<(\w+)>\w+</\w+>\n"
for line in in_file:
    line = line.strip()
    x = re.search(search_str,line)
    if x != None:
        y = re.findall('<(\w+)>',line)
        for item in y:
            column = re.findall('\w+',item)
            for col in column:
                columns.add(col)
col_list = list(columns)
#creat header
header_str = '\t'.join(col_list)
out_file.write(header_str + '\n')
print header_str
