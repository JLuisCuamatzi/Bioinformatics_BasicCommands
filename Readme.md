<b>Samtools commands</b>

cram to bam file

```
samtools view -b -T reference.fasta -o output-file.bam input_file.cram

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





