<b>Samtools commands</b>

bam file to cram file
```
samtools view -T reference.fasta -C -o output-file.cram input_file.bam

```


cram to bam file

```
samtools view -b -T reference.fasta -o output-file.bam input_file.cram

```

extract depth coverage

```
samtools depth -a -Q 30 input.bam > output.Q30.depth

```

<b>Conda commands</b>

* Create environment

```
conda create -n my.environment
```
* Activate conda env

```
conda activate my.environment

```

* Deactivate conda env
```
conda deactivate my.environment
```

<b>SubSet `bam` file </b>
 - Extract just a specific chromosome
```
samtools view input.bam "chr1" -b > subset.chr1.bam
samtools index subset.chr1.bam
```
 - Extract just a specific positions in a chromosome
```
samtools view input.bam "chr1:1000-1500" -b > subset.chr1.1000_1500.bam
samtools index subset.chr1.1000_1500.bam

```

<b> Convert a `fastq` file to a `fasta` file </b>
<br>
<br>
For this task, we will use a `python` script that use module `Bio`
 - This script requieres the next arguments:
   - <b>`fastq` input:</b> This input is indicated with the argument `-i`
   - <b>`fasta` output:</b> This input is indicated with the argument `-o`
```
cd bin/PyScripts/
python3 FastqToFasta.py -i /mnt/Guanina/lmorales/Public/Ustilago/data/fastq/clean/2021EE37_R1_clean.fastq.gz -o /mnt/Guanina/lmorales/Public/Ustilago/data/fastq/clean/asFasta/2021EE37_R1_clean.fasta

python3 FastqToFasta.py -i /mnt/Guanina/lmorales/Public/Ustilago/data/fastq/clean/2021EE37_R2_clean.fastq.gz -o /mnt/Guanina/lmorales/Public/Ustilago/data/fastq/clean/asFasta/2021EE37_R2_clean.fasta
```





