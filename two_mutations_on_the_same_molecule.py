import pysam
import itertools

def find_interesting_reads(bam_file,genome_limits,site,ref_seq):
    interesting_reads={}
    with pysam.AlignmentFile(bam_file, "rb") as bam:
        for read in bam.fetch():
            if read.reference_start<genome_limits[0] and read.reference_end>genome_limits[1]: #both forward and reverse mapping
                bases_to_read=site-read.reference_start #bases matched between read and reference, to iterate through to reach the site
                for (read_pos,reference_pos) in read.get_aligned_pairs():
                    if reference_pos!=None:
                        if bases_to_read==0:
                            if read_pos!=None:
                                if ref_seq==read.query_sequence[read_pos]:
                                    interesting_reads[read.query_name]=True
                                else:
                                    interesting_reads[read.query_name]=False
                            break
                        bases_to_read-=1 #reach the site we are interested in and see if it matches
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
            interesting_reads_one = find_interesting_reads(bam_file_path, genome_limits, interesting_sites[0], consensus_sites[0])
            interesting_reads_two = find_interesting_reads(bam_file_path, genome_limits, interesting_sites[1], consensus_sites[1])
            
            #print(len(interesting_reads_one.keys()))
            #print(len(interesting_reads_two.keys()))

            statistics={'just_first':0,'just_second':0,'both':0,'both_consensus':0}
            common_reads=[]
            for key1,key2 in itertools.zip_longest(interesting_reads_one.keys(),interesting_reads_two.keys()):
                #print(key1,key2)
                if (key1!=None) and (key1 in interesting_reads_two.keys()) and (key1 not in common_reads):
                    common_reads.append(key1)
                    if interesting_reads_one[key1]==True and interesting_reads_two[key1]==False:
                        statistics['just_first']+=1
                    if interesting_reads_one[key1]==False and interesting_reads_two[key1]==True:
                        statistics['just_second']+=1
                    if interesting_reads_one[key1]==False and interesting_reads_two[key1]==False:
                        statistics['both']+=1
                    if interesting_reads_one[key1]==True and interesting_reads_two[key1]==True:
                        statistics['both_consensus']+=1
                if (key2!=None) and (key2 in interesting_reads_one.keys()) and (key2 not in common_reads):
                    common_reads.append(key2)
                    if interesting_reads_one[key2]==True and interesting_reads_two[key2]==False:
                        statistics['just_first']+=1
                    if interesting_reads_one[key2]==False and interesting_reads_two[key2]==True:
                        statistics['just_second']+=1
                    if interesting_reads_one[key2]==False and interesting_reads_two[key2]==False:
                        statistics['both']+=1
                    if interesting_reads_one[key2]==True and interesting_reads_two[key2]==True:
                        statistics['both_consensus']+=1
            
            n=len(common_reads)
            print('number of reads that span the region with both mutations:',n)

            print(statistics)

            for i,v in statistics.items():
                statistics[i]=v/n
            
            print(statistics)