#open the input and output files
in_file_name = 'plantsvshuman_outmft6.csv'
out_file_name = 'plantsvshuman_selected.csv'
in_file = open(in_file_name, 'r')
out_file = open(out_file_name, 'w')

#loop though the lines in the input file
line_num = 0
for line in in_file:
    if line_num == 0:
        #write the header into the output file
	out_file.write(line)
        #find the indexes for T and Q colums
        line = line.strip('\n')
        colum_list = line.split('\t')
        end_q = colum_list.index('end_Q')
        start_q = colum_list.index('start_Q')
        end_t = colum_list.index('end_T')
        start_t = colum_list.index('start_T')
    else:
        #splitting the line into data fields
        line = line.strip('\n')
        data_list = line.split('\t')
        #caculate the length for query and target
        len_q = int(data_list[end_q]) - int(data_list[start_q])
        len_t = int(data_list[end_t]) - int(data_list[start_t])
        #find out the desire lines and write them into output file
        dif = len_q - len_t
        if dif == 0:
            out_file.write(line + '\n')
    line_num += 1

#close the files
in_file.close()
out_file.close()
