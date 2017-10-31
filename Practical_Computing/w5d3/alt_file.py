import os
import sys

testfilename = sys.argv[1]

def md5sum_syscall(filename):
    return os.popen('md5sum '+filename).read().split()[0]

myfiles = os.listdir('dna_files/')

target_md5sum = md5sum_syscall('dna.fa')

for temp_file in myfiles:
    temp_file_path = 'dna_files/' + temp_file
    temp_md5sum = md5sum_syscall(temp_file_path)
    if temp_md5sum == target_md5sum:
        print temp_file
