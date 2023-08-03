configfile: "config.yml"

nanopore_reads = 'data/nanopore/{phage}_{tag}.fastq.gz'

rule flye:
    input:
        reads = nanopore_reads
    output:
        flye_folder = directory('results/{phage}/assemblies/{tag}_flye'),
        assembly = 'results/{phage}/assemblies/{tag}.fasta'
    params:
        genome_size = lambda w : config["genome-size"][w.phage]
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

rule minimap:
    input:
        reads = nanopore_reads,
        reference = rules.flye.output.assembly
    output:
        alignment = 'results/{phage}/mapping/{tag}/{tag}.sam'
    conda:
        'conda_envs/phage_read_mapping.yml'
    shell:
        """
        minimap2 -ax map-ont {input.reference} \
            {input.reads} \
            > {output.alignment}
        """

rule bam:
    input:
        sam = rules.minimap.output.alignment
    output:
        bam = 'results/{phage}/mapping/{tag}/{tag}.bam',
        bai = 'results/{phage}/mapping/{tag}/{tag}.bam.bai'
    conda:
        'conda_envs/phage_read_mapping.yml'
    params:
        cores = 8
    shell:
        """
        samtools sort -@ {params.cores} \
            -o {output.bam} \
            {input.sam}
        samtools index {output.bam} \
            {output.bai}
        """

rule build_pileup:
    input:
        bam = rules.bam.output.bam
    output:
        pileup_folder = directory('results/{phage}/pileup/{tag}')
    conda:
        'conda_envs/pileup.yml'
    params:
        quality = 0,
        clip_length = 10
    shell:
        """
        python build_pileup.py --bam_file {input.bam} \
        --out_dir {output.pileup_folder} \
        --qual_min {params.quality} \
        --clip_minL {params.clip_length}
        """

rule all:
    input:
        assembly = expand(rules.build_pileup.output.pileup_folder,tag='new_chemistry',phage='EC2D2')