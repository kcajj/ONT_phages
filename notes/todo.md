# tasks
- [x] basics for the cluster
    - [x] conda
    - [x] git
    - [x] tmux (cheat sheet should be enough)
    - [x] slurm
        - [x] write a basic slurm script to run a py script
        - [x] run the script on the server
- [x] genome assembly
    - [x] flye
        - [x] documentation
        - [x] install
        - [x] run an assembly script in local
        - [x] run an assembly script with an interactive shell on the cluster
        - [x] run an assembly script submitting a job to the queue
    - [ ] miniasm
        - [x] documentation (documentation is too small, we will not use miniasm)
        - [x] install
        - [ ] send a job in the queue
    - [x] look at the reconstructed genome
        - [x] look at the assembly graph (useless, it's just a contig)
        - [x] align the reconstructed genome to a reference sequence of the phage
            - [x] blast the assembled genome to find the corresponding reference sequence
            - [x] align the reference with the assembled genome through minimap2 and look at the result
            - [x] align again the two sequences and build a sam file to look at the CIGARS
- [x] read mapping
    - [x] create sam file with minimap
        - [x] read minimap2 documentation
        - [x] send a minimap2 alignment to the job queue
    - [x] convert sam file to bam with samtools
        - [ ] read samtools documentation (too long, too many tools)
    - [x] look at the bam file on igv
    - [x] build the pileup of the alignment
        - [ ] understand the script
        - [ ] try to build your own pileup script
    - [x] extract and look at the information of the pileup (write a py script that plots the useful data)
        - [x] fastq integrity
        - [x] coverage
        - [x] non consensus frequency
        - [x] clips
        - [x] gaps

- [ ] blast the barcode on the raw data

- [ ] snakemake

- [ ] other timepoints

- [ ] pangraph