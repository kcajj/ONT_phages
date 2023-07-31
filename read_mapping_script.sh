mamba init
source ~/.bashrc
mamba activate phage_read_assembly

minimap2 -ax map-ont  \
    /scicore/home/neher/GROUP/data/Giacomo_analysis/raw_data/EC2D2_new_chemistry.fastq.gz \
    > results/EC2D2/alignment_reads_assembly.sam