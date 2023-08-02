import numpy as np

def convolution(array,k):
    return np.convolve(array,np.ones(k),mode='same')

def coverage(pileup):
    forward=pileup[0]
    reverse=pileup[1]
    l=np.shape(forward)[1]
    b=np.linspace(0,l,l)
    forward_coverage=np.zeros(l)
    reverse_coverage=np.zeros(l)
    for nuc_i,nuc in enumerate(forward):
        for pos,val in enumerate(nuc):
            forward_coverage[pos]+=forward[nuc_i,pos]
            reverse_coverage[pos]+=reverse[nuc_i,pos]
    return b,forward_coverage,reverse_coverage

def non_consensus_frequency(pileup,reference,k):
    forward=pileup[0]
    reverse=pileup[1]
    l=np.shape(forward)[1]
    b=np.linspace(0,l,l)
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
    
    cv_forward=convolution(forward_non_consensus_freq,k)/100
    cv_reverse=convolution(reverse_non_consensus_freq,k)/100

    return b,cv_forward,cv_reverse
                
def clips(pileup,clips_dict,k):
    l=np.shape(pileup)[2]
    b=np.linspace(0,l,l)
    
    forward_clips=np.zeros(l)
    reverse_clips=np.zeros(l)
    for pos,clip_data in clips_dict.items():
        pos=pos-1
        forward_clips[pos]=clip_data[2]
        reverse_clips[pos]=clip_data[3]
    
    cv_forward=convolution(forward_clips,k)
    cv_reverse=convolution(reverse_clips,k)
    return b,cv_forward,cv_reverse

def gaps(pileup,gap_dict,k):
    l=np.shape(pileup)[2]
    b=np.linspace(0,l,l)

    forward_gaps=np.zeros(l)
    reverse_gaps=np.zeros(l)
    for pos,gap_data in gap_dict.items():
        pos=pos-1
        for gap in gap_data.values():
            forward_gaps[pos]+=gap[0]
            reverse_gaps[pos]+=gap[1]
    
    cv_forward=convolution(forward_gaps,k)
    cv_reverse=convolution(reverse_gaps,k)
    return b,cv_forward,cv_reverse