#!/bin/bash
if [ $1 ]; then
    BLASTDATABASE=$1
else
    echo which BLAST database do you want to use?
    read BLASTDATABASE
fi     

if [ $2 ]; then
    INPUTFILE=$2
else
    echo which file contains the query sequence?
    read INPUTFILE
fi     

#remove the files from previous runs, if any
if [ -f blasthits.fasta ]; then
    rm blasthits.*
fi

BLASTHITS=`blastp -query $INPUTFILE -db $BLASTDATABASE -evalue 1e-3 -outfmt "6 sacc"`

for BLASTHIT in $BLASTHITS; do 
    blastdbcmd -db $BLASTDATABASE -entry $BLASTHIT 
done > blasthits.fasta

sed -i 's/>.*[|]/>/' blasthits.fasta

clustalo --in blasthits.fasta --outfmt=clustal > blasthits.clustal

#send any output that jalview produces to the trash (/dev/null)
jalview -open blasthits.clustal -colour clustal -nodisplay -png blasthits.png -imgMAP blasthits.html >& /dev/null

firefox blasthits.html
