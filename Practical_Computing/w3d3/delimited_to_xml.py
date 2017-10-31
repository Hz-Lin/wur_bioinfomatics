#open the input and output files
in_file_name = 'first_and_last_100_lines_crane_data.txt'
out_file_name = 'crane_data.xml'
in_file = open(in_file_name, 'r')
out_file = open(out_file_name, 'w')


#write the start of xml
start_string = '<?xml version="1.0" encoding="utf-8"?>\n<CraneData>\n'
out_file.write(start_string)


#write the events of xml
#loop though lines in the txt file
line_num = 0
for line in in_file:
    if line_num == 0:
        #creat a list of the colum names
        line = line.strip('\r\n')
        colum = line.split('\t')
    if line_num > 0:
        #creat start event tag
        out_file.write('<Event>\n')
        #splitting the line into data fields
        line = line.strip('\r\n')
        fields = line.split('\t')
        #creat properties
        field_num = 0
        for field in fields:
            #creat start properties tag
            start_tag = '<' + colum[field_num] + '>'
            #creat end properties tag
            end_tag = '</' + colum[field_num] + '>\n'
            #creat the whole properties string
            prop = start_tag + field + end_tag
            #write the properties string into xml
            out_file.write(prop)
            field_num += 1
        #creat end event tag
        out_file.write('</Event>\n')
    line_num += 1

#write the end of xml
end_string = '\n</CraneData>\n'
out_file.write(end_string)

#close the files
in_file.close()
out_file.close()
