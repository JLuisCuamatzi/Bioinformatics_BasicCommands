"""
@ description: 
@author: jcuamatzi

@ how to execute this script:

@ python3 
"""

# load module
from Bio import SeqIO

# define function to estimate GC percentage
def calculate_gc_percentage(sequence):
    sequence_length = len(sequence)
    gc_count = sequence.count('G') + sequence.count('C')
    gc_percentage = (gc_count / sequence_length) * 100
    return gc_percentage

# define function to calcuulate the GC in each sequence of a multie fasta file 
def calculate_gc_percentages_multi_fasta(input_file, output_file):
    with open(output_file, 'w') as f_out:
        for record in SeqIO.parse(input_file, 'fasta'):
            sequence = str(record.seq)
            gc_percentage = calculate_gc_percentage(sequence)
            f_out.write(f'{record.id}\t{gc_percentage:.2f}\n')



# Example usage:
input_filename = '/mnt/Timina/lmorales/Public/Ustilago/reference/USMA_521_v2/USMA_521_v2.fa'  # input file
output_filename = '/home/jcuamatzi/USMA_521_v2_GC_Percentage.txt'  # output file

calculate_gc_percentages_multi_fasta(input_filename, output_filename)


# Documentation:
calculate_gc_percentages_multi_fasta.__doc__ = "Function to estimate the GC percentage in each sequence of a multifasta file"
calculate_gc_percentage.__doc__ = "Function to estimate the GC percentage in a given DNA sequence"

