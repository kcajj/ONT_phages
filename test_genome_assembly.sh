mamba init
source ~/.bashrc
mamba env update --name phage_genome_assembly --file conda_envs/genome_assembly.yml --prune
mamba activate phage_genome_assembly

flye --nano-hq /scicore/home/neher/GROUP/data/Giacomo_analysis/raw_data/EC2D2_new_chemistry.fastq.gz \
    --out-dir output_genome_assembly --threads 4
