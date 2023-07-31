mamba init
source ~/.bashrc
mamba activate phage_read_mapping

minimap2 -ax map-ont  results/EC2D2/assembly.fasta\
    /scicore/home/neher/GROUP/data/Giacomo_analysis/raw_data/EC2D2_new_chemistry.fastq.gz \
    > results/EC2D2/alignment_reads_assembly.sam

samtools sort -@ 8 -o results/EC2D2/to_visualise.bam results/EC2D2/alignment_reads_assembly.sam