mamba init
source ~/.bashrc
mamba activate phage_read_mapping

minimap2 -ax map-ont  results_genome_assembly/EC2D2/assembly.fasta\
    /scicore/home/neher/GROUP/data/Giacomo_analysis/raw_data/EC2D2_new_chemistry.fastq.gz \
    > results_read_mapping/EC2D2/alignment_reads_assembly.sam

samtools sort -@ 8 -o results_read_mapping/EC2D2/bam_reads_assembly.bam results_read_mapping/EC2D2/alignment_reads_assembly.sam

samtools index results_read_mapping/EC2D2/bam_reads_assembly.bam results_read_mapping/EC2D2/bam_reads_assembly.bam.bai