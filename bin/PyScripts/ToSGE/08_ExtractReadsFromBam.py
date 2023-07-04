"""
@ autor: jcuamatzi
@ execute: python3 08_ExtractReadsFromBam.py -d /main/directory/ -f SampleID.csv -s Reads2Extract.20230620.csv


"""

import csv
import os
import argparse
import subprocess

ag = argparse.ArgumentParser()
ag = argparse.ArgumentParser(
    description = "Python scripts to write a SGE to extract reads from a bam/cram file",
    usage = "python3 file.py")

ag.add_argument("-d", "--directory", default = "/home/jcuamatzi", help = "path to the project directory")
ag.add_argument("-f", "--file", default = "", help = "csv with information of ID") # to read a csv file with sample imformation
ag.add_argument("-s", "--snpList", default = "", help = "csv with snp list")
#ag.add_argument("-b", "--batch", default = "1", help = "sequencing batch")
ag.add_argument("-i", "--inputsBam", default = "", help = "path to bam/cram files")

##

args = vars(ag.parse_args())
directory = str(args["directory"]) # 
Samples_List = args["file"]
SNP_List = str(args["snpList"])
#batch = str(args["batch"])
bam_path = str(args["inputsBam"])


# Read the file with sample names
samples_df = []
with open(Samples_List, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        samples_df.append(row)

# Read the file with SNP list
snp_df = []
with open(SNP_List, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        snp_df.append(row)

# Extract ChrToExtract column from snp_df
chr_to_extract = [row[0] for row in snp_df[1:]]

# Variables for SGE
std_log_dir = directory + "bin/SGE/08_ExtractReadsFromBam/log/"
if not os.path.exists(std_log_dir):
    os.makedirs(std_log_dir)
error_log = std_log_dir + "08_ExtractReadsFromBam.error.txt"
out_log = std_log_dir + "08_ExtractReadsFromBam.out.txt"

sge_file = directory + "bin/SGE/08_ExtractReadsFromBam/ExtReadsBamFiles.sge"

bam_path = directory + "data/bam/"
output_path = directory + "data/bam/SubsetToIGVVerification/SNPsPresentInSG200/"
if not os.path.exists(output_path):
    os.makedirs(output_path)
# Open the .sge file for writing

with open(sge_file, 'w') as file:
    file.write(f'#!/bin/bash\n') ## important!!! add \n at the end of each line
    file.write(f'## Use current working directory\n')
    file.write(f'#$ -cwd\n')
    file.write(f'. /etc/profile.d/modules.sh\n')
    file.write(f'##Error file\n')
    file.write(f'#$ -e {error_log}\n')
    file.write(f'##Out file\n')
    file.write(f'#$ -o {out_log}\n')
    file.write(f'#$ -S /bin/bash\n')
    file.write(f'## Job name\n')
    file.write(f'#$ -N ExtractingReads\n')
    file.write(f'#$ -l vf=4G\n')
    file.write(f'#$ -pe openmp 10\n')
    file.write(f'#$ -m e\n')
    file.write(f'source /etc/bashrc\n')
    file.write(f'## notification\n')
    file.write(f'#$ -M jcuamatzi@liigh.unam.mx\n')
    file.write(f'##\n')
    file.write(f'## Modules\n')
    file.write(f'module load htslib/1.2.1 samtools/1.9\n')
    file.write(f'\n')
    file.write(f'#\n')
    file.write(f'cd {bam_path}\n')
    #file.write(f'for files in *.cram; do samtools index $files; done \n')
    # Iterate over each sample in the second table
    for row in samples_df[1:]:
        sampleID = row[0]           # num of col with sample ID (2021EE01)
        sampleName = row[1]         # num of col with sample name (T20...)
        for element in chr_to_extract:
            # Write each element to the .sge file
            #file.write(f'#samtools view {sampleID}_{sampleName}_BWA.mrkdup.addgp.cram {element} -b > {output_path}{sampleID}_SubsetSharedSNP.Um10_{element}.bam\n') # batch 1 = .cram
            file.write(f'samtools view {sampleID}_{sampleName}_BWA.mrkdup.addgp.cram {element} -b > {output_path}{sampleID}_{element}.bam\n') # batch 2 = .bam
            file.write(f'samtools index {output_path}{sampleID}_{element}.bam\n')
    # to print out of for loop
    file.write(f'#\n')
    
# Execute automatically Sge file
subprocess.run(["qsub", sge_file])
