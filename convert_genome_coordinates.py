import pysam
from Bio import SeqIO

def is_matching(site,bam_file):
    matching=False
    with pysam.AlignmentFile(bam_file, "rb") as bam:
        for i, read in enumerate(bam):

            tot_len=0

            if matching==True: return matching,start,cigar

            for ic, (block_type, block_len) in enumerate(read.cigartuples):
                if tot_len+block_len>site:
                    if block_type==0:
                        matching=True
                        start=read.reference_start
                        cigar=read.cigartuples
                        break
                    #matching is false
                    start=read.reference_start
                    cigar=read.cigartuples
                    break
                if block_type!=2: tot_len+=block_len
    return matching,start,cigar

def convert_to_reference(site,start,cigar):
    tot_len=0
    insertions=0
    gaps=0
    clip=0
    for ic, (block_type, block_len) in enumerate(cigar):
        if tot_len+block_len>site:
            break
        if block_type==1: #insertion
            insertions+=block_len
        elif block_type==2: #deletion
            gaps+=block_len
        elif block_type==4: #softclip
            clip+=block_len
        elif block_type==5: #hardclip
            clip+=block_len
        tot_len+=block_len
    reference=start+site+gaps-clip-insertions
    return reference

def convert_coordinates(data):
    for phage, sites in data.items():
        bam_file=f'results/{phage}/mapping/reference/alignment_with_reference_new_chemistry.bam'
        for site in sites:
            matching,start,cigar=is_matching(site,bam_file)
            if matching:
                mapping=convert_to_reference(site,start,cigar)

                mapping=mapping+1 #frameshif due to python indexing

                output=f'the assembly site {str(site)} maps on the reference genome of {phage} at {str(mapping)}'
            else:
                output=f'There is no correspondance on the reference genome for assembly site {str(site)}'
            print(output)

            '''
            for assembly in SeqIO.parse(f'data/forward_assemblies/EM11_forward_assembly.fasta','fasta'):
                print(assembly.seq[site:site+10])
            
            for reference in SeqIO.parse(f'data/references/{phage}_reference.fasta','fasta'):
                print(reference.seq[mapping:mapping+10])
            '''

def convert_coordinate(phage, site):
    bam_file=f'results/{phage}/mapping/reference/alignment_with_reference_new_chemistry.bam'
    matching,start,cigar=is_matching(site,bam_file)
    if matching:
        mapping=convert_to_reference(site,start,cigar)

        mapping=mapping+1 #frameshif due to python indexing

        output=mapping
    else:
        output=None
    return output

#these are assembly sites (query of the bam alignment that we are considering) that show high non consensus frequency

if __name__=='__main__':

    data={'EC2D2':[],
       'EM11':[82280, 76089, 77655, 82934, 53019,    89018, 88770, 84164, 84167, 93601, 93605],
       'EM60':[79121, 50198, 50197,     71479, 87471, 73034, 73042]}
    
    convert_coordinates(data)