"""
@ how to execute this script:

@ cd /mnt/Guanina/lmorales/Public/Ustilago/bin/PyScripts/
@ python3 MedianCoverage.py -i /mnt/Guanina/lmorales/Public/Ustilago/analysis/03_Mapping/depth_coverage/2021EE01.Q30.depth.gz -o  /mnt/Guanina/lmorales/Public/Ustilago/2021EE08_coverage.test.txt -w 1000
"""


import argparse
import pandas as pd
import gzip
import time
import os
import sys

start_time = time.time()  # save the start time

# Create an argument to parse
parser = argparse.ArgumentParser(description='Calculate mean coverage for non-overlapping windows of 3.')

# indicate arguments for input output and window
parser.add_argument('-i', '--input', type=str, required=True, help='input file path')
parser.add_argument('-o', '--output', type=str, required=True, help='output file path')
parser.add_argument('-w', '--window_size', type=int, required=True, help='window size to estimate the median coverage')

args = parser.parse_args()

# check if input file exists
if os.path.isfile(args.input):
    print("Input file exists. The script will continue")
else:
    sys.exit("The input file does not exists. Bye")  

# Read the compressed gzip file into a df
column_names = ['Chr', 'Position', 'DepthCoverage']
with gzip.open(args.input, 'rt') as file:
    df = pd.read_csv(file, sep='\t', header=None, names=column_names)
    
# calculate the coverage median in all genome
coverage_median = df['DepthCoverage'].median()

# calculate mean coverage for non-overlapping windows of (window_size)
result = []
for chr_name, chr_group in df.groupby('Chr'):
    window_start = 1
    window_end = args.window_size
    while window_end <= chr_group['Position'].max():
        window_coverage = chr_group[(chr_group['Position'] >= window_start) & (chr_group['Position'] <= window_end)]['DepthCoverage']
        median_coverage = window_coverage.median()
        result.append({'chr': chr_name, 'window.start': window_start, 'window.end': window_end, 'window.median.coverage': median_coverage, 
                       'global.coverage.median': coverage_median})
        window_start += args.window_size
        window_end += args.window_size

# Create a DataFrame from the result
result_df = pd.DataFrame(result)

# estimate normalized coverage
result_df['normalized.coverage'] = result_df['window.median.coverage']/result_df['global.coverage.median']

# Save the result as a text file
result_df.to_csv(args.output, sep='\t', index=False)

# check thtat output file has a size > 0 kb
if os.path.isfile(args.output) and os.path.getsize(args.output) > 0:
    print("The output was successfully created")

# end
end_time = time.time()

# clculate the duration
duration = end_time - start_time

# Print the duration
print("Execution time:", duration, "seconds")
