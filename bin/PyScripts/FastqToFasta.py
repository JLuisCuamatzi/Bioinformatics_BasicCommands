"""
@ how to execute this script:

@ cd /mnt/Guanina/lmorales/Public/Ustilago/bin/PyScripts
@ python3 FastqToFasta.py -i /mnt/Guanina/lmorales/Public/Ustilago/data/fastq/clean/2021EE37_R2_clean.fastq.gz -o /mnt/Guanina/lmorales/Public/Ustilago/data/fastq/clean/asFasta/2021EE37_R2_clean.fasta
"""


import gzip
import argparse
from Bio import SeqIO

def fastq_gz_to_fasta(input_file, output_file):
    # Open the input gzip file and output file
    with gzip.open(input_file, "rt") as handle:
        with open(output_file, "w") as out_handle:
            # Iterate over the sequences in the compressed FASTQ file
            for record in SeqIO.parse(handle, "fastq"):
                # Write each sequence in FASTA format to the output file
                SeqIO.write(record, out_handle, "fasta")

# Arguments to read input and write output
parser = argparse.ArgumentParser(description="Convert FASTQ.gz to FASTA format")

parser.add_argument("-i", "--input", help="Input FASTQ.gz file", required=True) # input file argument
parser.add_argument("-o", "--output", help="Output FASTA file", required=True) # utput file argument

# Parse as flags arguments
args = parser.parse_args()

# Convert the fASTQ file to FASTA
fastq_gz_to_fasta(args.input, args.output)
