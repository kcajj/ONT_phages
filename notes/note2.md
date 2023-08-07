
we build a snakemake pipeline.

expand("text_{letter}_{num}.txt", num=[1, 2], allow_missing=True)


once the plots are ok we have to apply the filters on the basis of the distribution of quality and length, we will look at these properties in each sample.

## summary of the data up to now

### fastq statistics
1. the first sample has 32014 reads, with the following quality distribution (since we are working with hundreds of thousands of reads we won't be able to see these plot for the other ones, but we will just consider the score of every nucleotide taken as independent from the others.):

    ![fastqc_EC2D2](fastq_statistics/fastqc_EC2D2.png)

    the quality distribution of the nucleotides of this sample is the following:

    ![EC2D2_quality](fastq_statistics/EC2D2_quality)
    
    the length of the reads is:

    ![EC2D2_length](fastq_statistics/EC2D2_length)

2. the second sample has this nucleotide quality distribution, with 226,881 reads:

    ![EM11_quality](fastq_statistics/EM11_quality)

    and this read length distribution

    ![EM11_length](fastq_statistics/EM11_legth)

3. the third sample has this nucleotide quality distribution:

    ![EM60_quality](fastq_statistics/EM60_quality)

    and this read length distribution

    ![EM60_length](fastq_statistics/EM60_legth)

### clip length statistics

since we can also put a threshold on the length of the clips it can be useful to look at their distribution

1. 
    ![EC2D2_clip_length](images/clips_len_distr/EC2D2.png)
    n of clips 48814
    avg clip len 136.41524972343998
2.
    ![EM11_clip_length](images/clips_len_distr/EM11.png)
    291396
    98.28204917020138
3.
    ![EM60_clip_length](images/clips_len_distr/EM60.png)
    389662
    106.83263956967834

by looking at this data we can state that by filtering for a quality score bigger than 20 we can still keep the majority of the information in the reads.
to clear the data from the barcodes that would influence further analysis we can filter to exclude the clips shorter than 150 bp.


## analysis after the filtering

the plots after the filtering are:

nanopore qc
rename all envs