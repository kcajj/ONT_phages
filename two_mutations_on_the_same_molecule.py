import pysam
import matplotlib.pyplot as plt
from collections import defaultdict

def find_interesting_reads(bam_file,genome_limits):
    interesting_reads={}
    with pysam.AlignmentFile(bam_file, "rb") as bam:
        for read in bam.fetch():
            ##compute the gaps and insertions
            insertions=0
            gaps=0
            for ic, (block_type, block_len) in enumerate(read.cigar):
                if block_type==1: #insertion
                    insertions+=block_len
                elif block_type==2: #deletion
                    gaps+=block_len
            l=read.query_alignment_length
            if read.reference_start<genome_limits[0] and read.reference_start+l-insertions+gaps>genome_limits[1]: #both forward and reverse mapping
                interesting_reads[read.query_name]=[read.reference_start,read.cigar, read.query_alignment_sequence] #we take the clipped sequence (without softclips)
    return interesting_reads

if __name__ == "__main__":
    
    #phages=['EC2D2','EM11','EM60']
    #times=['new_chemistry','1','3','5']

    phages=['EM11']
    times=['3']
    interesting_sites=[82280, 76089]
    consensus_sites=['A','A']
    genome_limits=[75000,83000]

    for phage in phages:
        for time in times:
            
            bam_file_path = f'results/{phage}/mapping/new_chemistry/{time}.bam'
            interesting_reads = find_interesting_reads(bam_file_path, genome_limits)
            
            ######
            ###cleanup the sequence
            ######
            interesting_sequences={}
            for read_name, (start, cigar, sequence) in interesting_reads.items():
                tot_len=[0,0]
                insertions=[0,0]
                gaps=[0,0]
                for ic, (block_type, block_len) in enumerate(cigar):
                    if tot_len+block_len>interesting_sites[0]:
                        if block_type==0:
                            print(read_name)
                            interesting_sequences[read_name]=(start,sequence)
                            break
                        else:
                            print(block_type)
                            break
                    if block_type==1: #insertion
                        insertions+=block_len
                    elif block_type==2: #deletion
                        gaps+=block_len
                    tot_len+=block_len
            
            ###compute the frequencies

            n=len(interesting_sequences.keys())

            non_consensus_count={'just_1':0, 'just_2':0, 'both':0, 'consensus':0}

            for read_name, (start, sequence) in interesting_sequences.items():
                
                a=sequence[interesting_sites[0]-start]
                ca=consensus_sites[0]
                b=sequence[interesting_sites[1]-start]
                cb=consensus_sites[1]
                if a!=ca and b==cb:
                    non_consensus_count['just_1']+=1
                elif a==ca and b!=cb:
                    non_consensus_count['just_2']+=1
                elif a!=ca and b!=cb:
                    non_consensus_count['both']+=1
                elif a==ca and b==cb:
                    non_consensus_count['consensus']+=1


            print(non_consensus_count)
            print('number of reads that span the region with both mutations:',n)

            for key,value in non_consensus_count.items():
                non_consensus_count[key]=value/n

            print(non_consensus_count)