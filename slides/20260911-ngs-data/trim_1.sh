DATA_DIR=../../data/fastq

time fastp \
    -i $DATA_DIR/sample_1_R1_001.fastq.gz \
    -I $DATA_DIR/sample_1_R2_001.fastq.gz \
    -o sample_1_R1-trimmed.fastq.gz \
    -O sample_1_R2-trimmed.fastq.gz \
    -j sample_1.json \
    -h sample_1.html
