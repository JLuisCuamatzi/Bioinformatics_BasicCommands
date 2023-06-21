Python scripts to generate sge that are automatically executed in a HPC with `sge` as job gestor

<b> Extract an specific region (chr:start-end) from a `bam` alignment </b>

<b>Script =</b> 08_ExtractReadsFromBam.py

This script requires the next arguments:
 - <b>-d</b>: working directory. On this directory, the script creates subdirectories for sge files and/or outputs. Additionally, the path for inputs must be located inside this directory
 - <b>-f</b>: A sample sheet in `csv` format.
 - <b>-s</b>: List of coordinates to extract (preferibly as csv file).

Run the `python` script executing the next command:
```
python3 08_ExtractReadsFromBam.py -d /mnt/Guanina/lmorales/Public/Ustilago/ -f /mnt/Guanina/lmorales/Public/Ustilago/data/bam/SampleID.csv -s /mnt/Guanina/lmorales/Public/Ustilago/meta/Reads2Extract.20230620.csv
```
