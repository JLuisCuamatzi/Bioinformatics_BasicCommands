"""
@ how to execute this script:

@ cd /mnt/Guanina/lmorales/Public/Ustilago/bin/PyScripts
@ python3 GC_Percent_in_Windows.py -f /mnt/Guanina/lmorales/Public/Ustilago/blastn/Chr9/USMA_521_v2_9.fa -o /mnt/Guanina/lmorales/Public/Ustilago/USMA_521_v2_9_Analysis/USMA_521_v2_9_GC_10bp.txt
"""

import argparse

def calculate_gc_percent(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    gc_percent = (gc_count / len(sequence)) * 100
    return int(gc_percent)

def parse_fasta(fasta_file):
    sequences = []
    with open(fasta_file, 'r') as file:
        sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line
        if sequence:
            sequences.append(sequence)
    return sequences

def sliding_window(sequence, window_size):
    windows = []
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        windows.append(window)
    return windows

def calculate_gc_percent_windows(sequence, window_size):
    windows = sliding_window(sequence, window_size)
    results = []
    for i, window in enumerate(windows, start=1):
        start = i
        end = i + window_size - 1
        gc_percent = calculate_gc_percent(window)
        results.append((start, end, gc_percent))
    return results

def write_table_to_file(results, output_file):
    with open(output_file, 'w') as file:
        file.write('Start\tEnd\tGC%\n')
        for start, end, gc_percent in results:
            file.write(f'{start}\t{end}\t{gc_percent}\n') # the output will be writed delimited by tab

# main

parser = argparse.ArgumentParser(description='Calculate GC percentage in windows of 10 bp')
parser.add_argument('-f', '--fasta_input', type=str, help='Input FASTA sequence file') # input in fasta format (.fasta)
parser.add_argument('-o', '--output_table', type=str, help='Output table file') # output file 

# Parse command-line arguments
args = parser.parse_args()
fasta_file = args.fasta_input
output_file = args.output_table

# Parse FASTA file
sequences = parse_fasta(fasta_file)

# Process sequences
all_results = []
for i, sequence in enumerate(sequences, start=1):
    results = calculate_gc_percent_windows(sequence, 10)
    all_results.extend(results)

# Write results to output file

write_table_to_file(all_results, output_file)


