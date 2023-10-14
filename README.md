# ONT_phages

documentation of each script:

- build pileup: richard neher's script, rielaborated by Marco Molari and now rielaborated by me. it gives statistics on the non cons freq, gaps, insertions and clips.
- clips_length_distribution: this script takes in input the clip data of the pileup and plots the clip length distribution, it was useful to discover that the majority of clips had the same length (they were barcodes).
- convert_genome_coordinates: takes in input the bam file of the alignment between an assembly and a reference (the alignment must be forward alignment) and some coordinates of the assembly. returns the coordinates in the reference genome.
- fastq_statistics: takes in input the fastq files, it gives the distribution of the quality for each nucleotide of each read and the distribution of the length of each read. i was trying to plot a cumulative histogram for the distribution of the length but i stopped.
- frequencies_generator: takes in input the forward and reverse counts of the parameters of the alignments and returns the total frequencies after applying some thresholds.
- frequency_scores: uses the pileup data. uses frequencies generator to get the frequencies from pileup data, then stores the frequencies in a csv file. it can also plot the parameters distribution
- handle_npz_pkl: just opens some kind of files, also fasta.
- parameters_distribution: it can be used from the frequency_scores script, it takes the pileup counts and just plots the distributions of the variables involved in the thresholds.
- pileup_analysis: takes pileup results and plots some genome wide overview of the counts.
- plot_storage: useful to store the plots of the pileup analysis
- secondary_mapping: creates the plots of the relationships between primary and secondary mapping reads.
- time_analysis: most important script. takes the csv file with the scores and builds the time analysis. it plots the distribution of the scores for each parameter over time. for each parameter it plots the frequency variation over the 3 timesteps, of the sites that show the best variation.
- two mutations on the same molecule: takes in input a couple of positions of the assembly in which we found some mutations after the time analysis. it also takes the consensus base in the assembly. it computes how many reads span the two mutation sites, and what is the distribution of the two mutations on those reads.
