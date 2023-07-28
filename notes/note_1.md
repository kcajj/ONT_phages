## consensus assembly

tools:
- flye: https://github.com/fenderglass/Flye
- miniasm: https://github.com/lh3/miniasm (minipolish? https://github.com/rrwick/Minipolish)

## flye

input reads can be fasta, fastq compressed or not.

--meta option for metagenome/uneven coverage assembly

flye polisher: --polish-target

supported technologies: oxford nanopore (--nano-raw works for most datasets, for nanopore basecalled with guppy5+ weuse --nano-hq if we have q20 data we use --nano-hq and --read-error 0.03. with error corrected ont reads we use --nano-corr) and pac bio (--pacbio-raw)

flye doesn't require any data preparation

haplotype mode keeps some bubbles.

--scaffold to add scaffolding

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


