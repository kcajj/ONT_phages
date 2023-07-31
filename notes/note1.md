
we have finally the first assembly of a phage genome.

we have assembled the EC2D2_new_chemistry.fastq.gz reads. with a reference genome of approximately 163kb

we have used the following flye command:
flye --nano-hq /scicore/home/neher/GROUP/data/Giacomo_analysis/raw_data/EC2D2_new_chemistry.fastq.gz \
    --out-dir output_genome_assembly --threads 4 --genome-size 0.163m --asm-coverage 40

we have obtained the following output:
#seq_name	length	cov.	circ.	repeat	mult.	alt_group	graph_path
contig_1	150850	637	N	N	1	*	*,1,*

the sequence doesn't result to be circular, but looking at the alignment with a reference we found a shift.
the reference is: https://www.ncbi.nlm.nih.gov/nuccore/MZ501100.1?report=fasta, found by blasting the actual sequence.

the result of the alignment between assembly and reference is: (using minimap2 database_virus_genome.fasta assembly.fasta)
distinct minimizers: 28086 (99.85% are singletons); average occurrences: 1.002; average spacing: 5.346; total length: 150425
contig_1	150850	55881	150842	+	MZ501100.1	150425	7	94968	94930	94961	60	tp:A:P	cm:i:17750	s1:i:94930	s2:i:0	dv:f:0.0000	rl:i:0
contig_1	150850	127	55874	+	MZ501100.1	150425	94678	150425	55722	55747	60	tp:A:P	cm:i:10429	s1:i:55722	s2:i:0	dv:f:0.0000	rl:i:0

we can produce a sam to take a look at the cigar:
contig_1	0	MZ501100.1	1	60	55874S94975M1S	*	0	0
NM:i:3	ms:i:189932	AS:i:189932	nn:i:0	tp:A:P	cm:i:17750	s1:i:94930	s2:i:0	de:f:0.0000	SA:Z:MZ501100.1,94675,+,123S55751M94976S,60,3;	rl:i:0

contig_1	2048	MZ501100.1	94675	60	123H55751M94976H	*	0	0
tp:A:P	cm:i:10429	s1:i:55722	s2:i:0	de:f:0.0001	SA:Z:MZ501100.1,1,+,55874S94975M1S,60,3;	rl:i:0


now 