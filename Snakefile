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
        cores = 4
        coverage = 40
    conda:
        'conda_envs/phage_genome_assembly.yml'
    shell:
        """
        flye --nano-hq {input.reads} \
            --out-dir {output.flye_folder} \
            --threads {params.cores} \
            --genome-size {params.genome_size} \
            --asm-coverage {params.coverage}
        
        cp {output.flye_folder}/assembly.fasta {output.assembly}
        """

rule minimap:
    input:
        reads = lambda w : expand(rules.flye.input.reads, tag=w.qry_tag, phage=w.phage),
        reference = lambda w : expand(rules.flye.output.assembly, tag=w.ref_tag, phage=w.phage)
    output:
        alignment = 'results/{phage}/mapping/{ref_tag}/{qry_tag}.sam'
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
        bam = 'results/{phage}/mapping/{ref_tag}/{qry_tag}.bam',
        bai = 'results/{phage}/mapping/{ref_tag}/{qry_tag}.bam.bai'
    conda:
        'conda_envs/phage_read_mapping.yml'
    params:
        cores = 4
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
        pileup_folder = directory('results/{phage}/pileup/{ref_tag}/{qry_tag}')
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

rule plot_pileup:
    input:
        pileup_folder = rules.build_pileup.output.pileup_folder,
        ref = lambda w : expand(rules.flye.output.assembly, tag=w.ref_tag, phage=w.phage)
    output:
        plot_folder = directory('plots/{phage}/{ref_tag}/{qry_tag}')
    conda:
        'conda_envs/pileup.yml'
    shell:
        """
        python pileup_analysis.py --in_dir {input.pileup_folder} \
            --ref {input.ref} \
            --out_dir {output.plot_folder}
        """

rule all:
    input:
        assembly = expand(rules.plot_pileup.output.plot_folder,ref_tag='new_chemistry',qry_tag='new_chemistry',phage='EC2D2')