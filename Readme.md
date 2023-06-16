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
<b>SubSet `bam` file </b>
```
samtools view input.bam "chr1" -b > subset.chr1.bam
samtools index subset.chr1.bam
```

* Activate conda env

```
conda activate my.environment

```

* Deactivate conda env
```
conda deactivate my.environment
```
