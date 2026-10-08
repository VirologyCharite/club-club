#!/bin/bash

data=/sc-projects/sc-proj-cc11-civclub/club-club/data

samtools mpileup -d 0 -aa -A -B -Q 0 \
    --fasta-ref $data/references/NC_055231.1.fasta \
    $data/bam/mapped-to-NC_055231.1.bam \
    | ivar consensus -p consensus -q 20 -t 0.6 -m 5
