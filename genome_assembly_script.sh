mamba init
source ~/.bashrc
mamba activate phage_genome_assembly

flye --nano-hq /scicore/home/neher/GROUP/data/Giacomo_analysis/raw_data/EC2D2_new_chemistry.fastq.gz \
    --out-dir output_genome_assembly --threads 4 --genome-size 0.163m --asm-coverage 40