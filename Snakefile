

rule flye:
    input:
        reads = 'data/nanopore/{phage}_{tag}.fastq.gz'
    output:
        flye_folder = directory('results/{phage}/assemblies/{tag}_flye'),
        assembly = 'results/{phage}/assemblies/{tag}.fasta'
    params:
        genome_size = '0.163m'
    conda:
        'conda_envs/phage_genome_assembly.yml'
    shell:
        """
        flye --nano-hq {input.reads} \
            --out-dir {output.flye_folder} \
            --threads 4 \
            --genome-size {params.genome_size} \
            --asm-coverage 40
        
        cp {output.flye_folder}/assembly.fasta {output.assembly}
        """
    
rule all:
    input:
        assembly = expand(rules.flye.output.assembly,tag='new_chemistry',phage='EC2D2')