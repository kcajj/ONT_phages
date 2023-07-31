## consensus assembly

tools:
- flye: https://github.com/fenderglass/Flye
- miniasm: https://github.com/lh3/miniasm (minipolish? https://github.com/rrwick/Minipolish)

## flye

input reads can be fasta, fastq compressed or not. flye doesn't require any data preparation.

supported technologies: oxford nanopore (--nano-raw works for most datasets, for nanopore basecalled with guppy5+ weuse --nano-hq if we have q20 data we use --nano-hq and --read-error 0.03. with error corrected ont reads we use --nano-corr) and pac bio (--pacbio-raw)

--genome-size better to specify it (ex. 0.163m)

--asm-coverage together with genome size mandatory, we aim for 40x coverage

--meta option for metagenome/uneven coverage assembly

--polish-target

--scaffold to add scaffolding

--haplotype mode keeps some bubbles.

outputs:
- assembly.fasta: final assembly
- assembly_graph.gv: final repeat graph.
- assembly_info.txt: info about contigs
    - Contig/scaffold id
    - Length
    - Coverage
    - Is circular, (Y)es or (N)o
    - Is repetitive, (Y)es or (N)o
    - Multiplicity (based on coverage)
    - Alternative group
    - Graph path (graph path corresponding to this contig/scaffold).
    - Scaffold gaps are marked with ?? symbols, and * symbol denotes a terminal graph node.

which graphs do flye use? The Flye algorithms are using repeat graph as a core data structure. In difference to de Bruijn graphs which require exact k-mer matches, repeat graphs are built using approximate sequence matches, thus can tollerate higher noise of SMS reads.
The edges of repeat graph represent genomic sequence, and nodes define the junctions. All edges are classified into unique and repetitive. The genome traverses the graph in an unknown way, so as each unique edge appears exactly once in this traversal. Repeat graphs are useful for repeat analysis and resolution - which are one of the key genome assembly challenges.

a thread is an independent set of operations of an algorithm, a thread is computed thorugh a core, each core can compute only one thread at a time. if we have 8 threads and 8 cores, 8 independent parts of the algorithm will be executed at the same time. we usually want to have the same number of cores and threads.

### quick

'''
usage: flye (--pacbio-raw | --pacbio-corr | --pacbio-hifi | --nano-raw |
	     --nano-corr | --nano-hq ) file1 [file_2 ...]
	     --out-dir PATH

	     [--genome-size SIZE] [--threads int] [--iterations int]
	     [--meta] [--polish-target] [--min-overlap SIZE]
	     [--keep-haplotypes] [--debug] [--version] [--help] 
	     [--scaffold] [--resume] [--resume-from] [--stop-after] 
	     [--read-error float] [--extra-params]

Assembly of long reads with repeat graphs

optional arguments:
  -h, --help            show this help message and exit
  --pacbio-raw path [path ...]
                        PacBio regular CLR reads (<20% error)
  --pacbio-corr path [path ...]
                        PacBio reads that were corrected with other methods (<3% error)
  --pacbio-hifi path [path ...]
                        PacBio HiFi reads (<1% error)
  --nano-raw path [path ...]
                        ONT regular reads, pre-Guppy5 (<20% error)
  --nano-corr path [path ...]
                        ONT reads that were corrected with other methods (<3% error)
  --nano-hq path [path ...]
                        ONT high-quality reads: Guppy5+ SUP or Q20 (<5% error)
  --subassemblies path [path ...]
                        [deprecated] high-quality contigs input
  -g size, --genome-size size
                        estimated genome size (for example, 5m or 2.6g)
  -o path, --out-dir path
                        Output directory
  -t int, --threads int
                        number of parallel threads [1]
  -i int, --iterations int
                        number of polishing iterations [1]
  -m int, --min-overlap int
                        minimum overlap between reads [auto]
  --asm-coverage int    reduced coverage for initial disjointig assembly [not set]
  --hifi-error float    [deprecated] same as --read-error
  --read-error float    adjust parameters for given read error rate (as fraction e.g. 0.03)
  --extra-params extra_params
                        extra configuration parameters list (comma-separated)
  --plasmids            unused (retained for backward compatibility)
  --meta                metagenome / uneven coverage mode
  --keep-haplotypes     do not collapse alternative haplotypes
  --no-alt-contigs      do not output contigs representing alternative
                        haplotypes
  --scaffold            enable scaffolding using graph [disabled by default]
  --trestle             [deprecated] enable Trestle [disabled by default]
  --polish-target path  run polisher on the target sequence
  --resume              resume from the last completed stage
  --resume-from stage_name
                        resume from a custom stage
  --stop-after stage_name
                        stop after the specified stage completed
  --debug               enable debug output
  -v, --version         show program's version number and exit
'''

## miniasm

- Overlap for PacBio reads (or use "-x ava-ont" for nanopore read overlapping)
  minimap2/minimap2 -x ava-pb -t8 pb-reads.fq pb-reads.fq | gzip -1 > reads.paf.gz
- Layout
  miniasm/miniasm -f reads.fq reads.paf.gz > reads.gfa

## files

EC2D2_old_chemistry.fastq.gz
EC2D2_new_chemistry.fastq.gz
EC2D2_1.fastq.gz
EC2D2_3.fastq.gz
EC2D2_5.fastq.gz
EM11_old_chemistry.fastq.gz
EM11_new_chemistry.fastq.gz
EM11_1.fastq.gz
EM11_3.fastq.gz
EM11_5.fastq.gz
EM60_old_chemistry.fastq.gz
EM60_new_chemistry.fastq.gz
EM60_1.fastq.gz
EM60_3.fastq.gz
EM60_5.fastq.gz

EC2D2 phage: genome size = 163 kb