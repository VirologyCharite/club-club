DATA_DIR=../../data/fastq

time fastp \
    -i $DATA_DIR/sample_2_R1_001.fastq.gz \
    -I $DATA_DIR/sample_2_R2_001.fastq.gz \
    -o sample_2_R1-trimmed.fastq.gz \
    -O sample_2_R2-trimmed.fastq.gz \
    -j sample_2.json \
    -h sample_2.html
