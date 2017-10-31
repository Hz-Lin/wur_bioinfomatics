# First import all necessary modules
import sys
from subprocess import check_call, check_output

import subprocess

def check_output_ext (command, shell=False):
    try:
        output = subprocess.check_output (command, shell=shell)
    except subprocess.CalledProcessError as e:
        output = e.output
    return output

# Put all fixed filenames (and other constants) here
all_outputs = 'blasthits.*' # used by rm

if len(sys.argv) > 1: # will not work properly inside notebook...
    blast_database = sys.argv[1]
else:
    blast_database = raw_input('which BLAST database do you want to use? ')
    
if len(sys.argv) > 2: # will not work properly inside notebook...
    input_filename = sys.argv[2]
else:
    input_filename = raw_input('which file contains the query sequence? ')

print blast_database
print input_filename

# Removeing old output
command = 'ls %s' % all_outputs
output = check_output_ext(command, shell=True)
print '--- start of output ---\n' + output + '--- end of output ---'

if len(output) > 0:
    print 'something to be removed'
    command = 'rm %s' % all_outputs
    check_call(command, shell=True)
else:
    print 'nothing to do'

# obtaining the blast hits
blast_query_command = 'blastp -query %s -db %s -evalue 1e-3 -outfmt "6 sacc"'
command = blast_query_command % (input_filename,blast_database)
output = check_output(command, shell=True)
print len(output)
print output[:300]

# turn the output into a list
blast_hits = output.strip().split('\n')
print blast_hits
# print the elements of the list
for hit in blast_hits:
    print hit

# combining the blast hits
fasta_filename = 'blasthits.fasta'
fasta_file = open(fasta_filename, 'w')
for hit in blast_hits:
    blast_command = 'blastdbcmd -db %s -entry "%s"'
    # TODO: Fill in variable parts of command
    command = blast_command % (blast_database,hit)
    output = check_output(command, shell=True)
    fasta_file.write(output)
fasta_file.close()

# Use check_output() to look into the fasta_file.
command = 'cat %s' % (fasta_filename)
output = check_output(command, shell=True)
print output

# reformatting blasthits.fasta
# Define names for further files
main_name = fasta_filename.split('.')
clustal_filename = main_name[0]+'.clustal'
png_filename = main_name[0]+'.png'
html_filename = main_name[0]+'.html'

clustalo_command = 'clustalo --in %s --outfmt=clustal > %s'
command = clustalo_command % (fasta_filename,clustal_filename)
check_call(command, shell=True)

jal_command = 'jalview -open %s -colour clustal -nodisplay -png %s -imgMAP %s'
command = jal_command % (clustal_filename,png_filename,html_filename)
check_call(command, shell=True)

firefox_command = 'firefox %s'
command = firefox_command % html_filename
check_call(command, shell=True)