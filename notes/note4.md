# biological interpretation

our results so far

possible biological meaning


















red line in fastq quality

are methylation sites increasing?

! va bene la finestra dei pileup plots? 
vanno bene le thresholds delle frequenze? no

score on the basis of an entropy, if there is less disorder we give more power to the observation


36619 reference site with high ncf, corresponds to 79121 in my assembly
this ite has coverage <100 and divergence between forward and reverse at timepoint 1 is 0.33

put the axis names in the time analysis

hello, i have some updates regarding what we discussed yesterday:

1. the analysis of the mutations on the same read was wrong, i was assuming to have reads without gaps. below there are the new results, i believe that they make more sense given the data of the time analysis graphs.
    <pre>
    phages=['EM11']
    times=['3']
    interesting_sites=[82280, 76089]
    consensus_sites=['A','A']
    genome_limits=[75000,83000]

    number of reads that span the region with both mutations: 294
    {'just_first': 10, 'just_second': 27, 'both': 145, 'both_consensus': 112}
    {'just_first': 0.034013605442176874, 'just_second': 0.09183673469387756, 'both': 0.4931972789115646, 'both_consensus': 0.38095238095238093}
    </pre>
    <pre>
    phages=['EM11']
    times=['5']
    interesting_sites=[82280, 76089]
    consensus_sites=['A','A']
    genome_limits=[75000,83000]

    number of reads that span the region with both mutations: 196
    {'just_first': 9, 'just_second': 15, 'both': 112, 'both_consensus': 60}
    {'just_first': 0.04591836734693878, 'just_second': 0.07653061224489796, 'both': 0.5714285714285714, 'both_consensus': 0.30612244897959184}
    </pre>
    <pre>
    phages=['EM11']
    times=['1']
    interesting_sites=[77655, 82934]
    consensus_sites=['A','G']
    genome_limits=[76000,83000]

    number of reads that span the region with both mutations: 214
    {'just_first': 8, 'just_second': 10, 'both': 75, 'both_consensus': 121}
    {'just_first': 0.037383177570093455, 'just_second': 0.04672897196261682, 'both': 0.35046728971962615, 'both_consensus': 0.5654205607476636}
    </pre>

2. the site of EM60 that you found (36619) corresponds to 79121 in my assembly and i discarded it because the coverage was less than 50 and the difference between forward and reverse frequency is 0.33 at timepoint 1. I corrected the thresholds and now i have it in the plot.

3. the sites with non consensus frequency of 0.4 that I found in EM60 map at 7695 and 7696 in the reference genome. they are part of the major capisd protein, they are the first two positions of the last codon of the gene.

4. the sites with gap frequency at 0.3 that I found in EM60 map at 28977 and 44969 in the reference genome. they are part of lateral tail fiber proteins

5. I tried to put a low threshold on the score of the first timepoint but nothing fancy happened

6. I noticed that in the non consensus frequency graph of EM11 there is a site that follows a similar path as the two i found in EM60 (reaching .3 of non consensus frequency). it maps at 7328 on the reference, part of major capsid protein gene.