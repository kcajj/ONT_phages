# read mapping

tools:
- minimap2

## minimap2

minimap takes a reference database and a query and produces approximate mapping in paf format. the input can be compressed or not.

-c: provides cigar

-a: outputs alignments in sam format

It is usually recommended to choose a preset with option -x, which sets multiple parameters at the same time. The default setting is the same as map-ont.

minimap2 -ax map-ont ref.fa ont-reads.fq > aln.sam      # for Oxford Nanopore reads

### minimiser index
to save time we can save the index with option -d and replace the reference sequence file with the index file on the minimap2 command line:
<pre>
minimap2 -d ref.mmi ref.fa
minimap2 -a ref.mmi reads.fq > alignment.sam
</pre>

### Overlaps between long reads

minimap2 -x ava-pb  reads.fq reads.fq > ovlp.paf    # PacBio CLR read overlap
minimap2 -x ava-ont reads.fq reads.fq > ovlp.paf    # Oxford Nanopore read overlap

Similarly, ava-pb uses HPC minimizers while ava-ont uses ordinary minimizers. It is usually not recommended to perform base-level alignment in the overlapping mode because it is slow and may produce false positive overlaps. However, if performance is not a concern, you may try to add -a or -c anyway.

### paired end alignment

minimap2 -ax sr ref.fa read1.fq read2.fq > aln.sam     # paired-end alignment

When two read files are specified, minimap2 reads from each file in turn and merge them into an interleaved stream internally. Two reads are considered to be paired if they are adjacent in the input stream and have the same name (with the /[0-9] suffix trimmed if present). Single- and paired-end reads can be mixed.

### algorithm

minimap2 works with hash tables, it hashes the reference sequence and then maps the queries.

### quick
<pre>

# long sequences against a reference genome
./minimap2 -a test/MT-human.fa test/MT-orang.fa > test.sam
# create an index first and then map
./minimap2 -x map-ont -d MT-human-ont.mmi test/MT-human.fa
./minimap2 -a MT-human-ont.mmi test/MT-orang.fa > test.sam
# use presets (no test data)
./minimap2 -ax map-pb ref.fa pacbio.fq.gz > aln.sam       # PacBio CLR genomic reads
./minimap2 -ax map-ont ref.fa ont.fq.gz > aln.sam         # Oxford Nanopore genomic reads
./minimap2 -ax map-hifi ref.fa pacbio-ccs.fq.gz > aln.sam # PacBio HiFi/CCS genomic reads (v2.19 or later)
./minimap2 -ax asm20 ref.fa pacbio-ccs.fq.gz > aln.sam    # PacBio HiFi/CCS genomic reads (v2.18 or earlier)
./minimap2 -ax sr ref.fa read1.fa read2.fa > aln.sam      # short genomic paired-end reads
./minimap2 -ax splice ref.fa rna-reads.fa > aln.sam       # spliced long reads (strand unknown)
./minimap2 -ax splice -uf -k14 ref.fa reads.fa > aln.sam  # noisy Nanopore Direct RNA-seq
./minimap2 -ax splice:hq -uf ref.fa query.fa > aln.sam    # Final PacBio Iso-seq or traditional cDNA
./minimap2 -ax splice --junc-bed anno.bed12 ref.fa query.fa > aln.sam  # prioritize on annotated junctions
./minimap2 -cx asm5 asm1.fa asm2.fa > aln.paf             # intra-species asm-to-asm alignment
./minimap2 -x ava-pb reads.fa reads.fa > overlaps.paf     # PacBio read overlap
./minimap2 -x ava-ont reads.fa reads.fa > overlaps.paf    # Nanopore read overlap
# man page for detailed command line options
man ./minimap2.1

</pre>