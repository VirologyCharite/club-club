#!/bin/bash

#SBATCH --cpus-per-task=64
#SBATCH --time=12:00:00
#SBATCH --mem=128G

pixi run bowtie2 \
     --threads $SLURM_CPUS_PER_TASK \
    --local --xeq --no-unal -x ../20260918-map/HBV \
    -1 ~/data/fastq/LV7008876184-LV7008414499-CGG2015787_S1_L002_R1_001-ar3.fastq.gz \
    -2 ~/data/fastq/LV7008876184-LV7008414499-CGG2015787_S1_L002_R2_001-ar3.fastq.gz \
    > matches-local-big-FASTQ.sam
