import pysam

def process_sam(sam_file):
    #for each contig find the starting point and the cigar
    return cigars

def is_matching(site,cigars):
    matching=False
    for start,cigar in cigars.items():
        #compute if the site is in a matching region
        return matching,start,cigar

def convert_to_reference(site,start,cigar):
    insertions='insertions preceeding the mapping position'
    clip='clip preceeding the mapping position'
    gaps='gaps preceeding the mapping position'
    reference=start+site+gaps-clip-insertions
    return reference

sites=[12]
sam_file='file'

#cigars is a dicitonary in which the keys are the starting sites, the values are the cigar strings
cigars=process_sam(sam_file)

for site in sites:
    matching,start,cigar=is_matching(site,cigars)
    if matching:
        reference=convert_to_reference(site,start,cigar)
