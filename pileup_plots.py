import numpy as np

def coverage(pileup,l):
    forward=pileup[0]
    reverse=pileup[1]
    forward_coverage=np.zeros(l)
    reverse_coverage=np.zeros(l)
    for nuc_i,nuc in enumerate(forward):
        for pos,val in enumerate(nuc):
            forward_coverage[pos]+=forward[nuc_i,pos]
            reverse_coverage[pos]+=reverse[nuc_i,pos]
    return forward_coverage,reverse_coverage

def non_consensus_frequency(pileup,reference,l):
    forward=pileup[0]
    reverse=pileup[1]
    alphabet='ACGT-N'
    forward_non_consensus_freq=np.zeros(l)
    reverse_non_consensus_freq=np.zeros(l)

    for pos,ref_nuc in enumerate(reference):
        forward_non_consensus=0
        forward_total=0
        reverse_non_consensus=0
        reverse_total=0
        for i_nuc,nuc in enumerate(alphabet):
            forward_total+=forward[i_nuc][pos]
            reverse_total+=reverse[i_nuc][pos]
            if not nuc==ref_nuc:    
                forward_non_consensus+=forward[i_nuc][pos]
                reverse_non_consensus+=reverse[i_nuc][pos]
        forward_non_consensus_freq[pos]=forward_non_consensus/forward_total
        reverse_non_consensus_freq[pos]=reverse_non_consensus/reverse_total

    return forward_non_consensus_freq,reverse_non_consensus_freq
                
def clips(clips_dict,l):
    forward_clips=np.zeros(l)
    reverse_clips=np.zeros(l)
    for pos,clip_data in clips_dict.items():
        pos=pos-1
        forward_clips[pos]=clip_data[2]
        reverse_clips[pos]=clip_data[3]

    return forward_clips,reverse_clips

def gaps(gap_dict,l):
    forward_gaps=np.zeros(l)
    reverse_gaps=np.zeros(l)
    for pos,gap_data in gap_dict.items():
        pos=pos-1
        for gap in gap_data.values():
            forward_gaps[pos]+=gap[0]
            reverse_gaps[pos]+=gap[1]
    
    return forward_gaps,reverse_gaps