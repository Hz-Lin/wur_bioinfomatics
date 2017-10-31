#open the input and output files
in_file_name = 'some_crane_data.xml'
out_file_name = 'some_crane_data.csv'
in_file = open(in_file_name,'r')
out_file = open(out_file_name, 'w')

import re

#creat a set of column names
columns = set()
search_str = '<(\w+)>\w+</\w+>\n'
for line in in_file:
    line = line.strip
    x = re.search(search_str,line)
    if x != None:
        y = re.findall('<(\w+)>',line)
        for item in y:
            column = re.findall('\w+',item)
            for col in column:
                columns.add(col)

#creat header
col_list = list(columns)
header_str = '\t'.join(col_list)
out_file.write(header_str + '\n')
print header_str


#extract values
for line in in_file:
    line = line.strip
    x = re.search(search_str,line)
    if line == '<Event>':
        #reset the list of all the values in a line
        val_line = []
    if x != None:
        #properties lines, extract values
        y = re.findall('>(\w+)<',line)
        for item in y:
            vals = re.findall('\w+',item)
            for v in vals:
                val_line.append(val)
    if line == '</Event>':
        #end of a line for csv, creat a line in output file
        new_line_list = []
        for col in column:
            col_index = column.index(col)
            for va in val_line:
                va_index = val_line.index(va)
                if va_index == col_index:
                    new_line_list.append(va)
        new_line = '\t'.join(new_line_list)
        out_file.write(new_line + '\n')
        print new_line            

in_file.close()
out_file.close()
