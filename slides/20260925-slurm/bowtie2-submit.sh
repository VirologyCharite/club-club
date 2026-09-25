#!/bin/bash

#SBATCH --cpus-per-task=32
#SBATCH --time=1:00:00
#SBATCH --mem=16G

# You can get into a pixi shell like this (for all commands)
# eval "$(pixi shell-hook --manifest-path ~/workspace/pixi.toml --shell bash)"

# Or just use 'pixi run' before your commands.
pixi run bowtie2 \
    --threads $SLURM_CPUS_PER_TASK \
    --local --xeq --no-unal -x ../20260918-map/HBV \
    -1 ~/data/fastq/HBV_RISE718_R1_trimmed.fastq.gz \
    -2 ~/data/fastq/HBV_RISE718_R2_trimmed.fastq.gz \
    -U ~/data/fastq/HBV_RISE718_single_trimmed.fastq.gz \
    > matches-local-with-single.sam
