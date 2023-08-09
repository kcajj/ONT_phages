import numpy as np
from pileup_plots import coverage,clips,insertions,gaps

def ncf(pileup, reference, l):
    forward=pileup[0]
    reverse=pileup[1]
    alphabet='ACGT-N'
    forward_non_consensus_freq=np.zeros(l)
    reverse_non_consensus_freq=np.zeros(l)
    non_consensus_freq=np.zeros(l)

    for pos,ref_nuc in enumerate(reference):
        forward_non_consensus=0
        forward_total=0
        reverse_non_consensus=0
        reverse_total=0
        non_consensus=0
        total=0
        for i_nuc,nuc in enumerate(alphabet):
            forward_total+=forward[i_nuc][pos]
            reverse_total+=reverse[i_nuc][pos]
            total+=forward[i_nuc][pos]+reverse[i_nuc][pos]
            if not nuc==ref_nuc:
                forward_non_consensus+=forward[i_nuc][pos]
                reverse_non_consensus+=reverse[i_nuc][pos]
                non_consensus+=forward[i_nuc][pos]+reverse[i_nuc][pos]

        forward_non_consensus_freq[pos]=forward_non_consensus/forward_total
        reverse_non_consensus_freq[pos]=reverse_non_consensus/reverse_total
        non_consensus_freq[pos]=non_consensus/total

    return forward_non_consensus_freq,reverse_non_consensus_freq,non_consensus_freq

def get_total_mappings(clips_dict,l):
    forward_mappings=np.zeros(l)
    reverse_mappings=np.zeros(l)
    for pos,clip_data in clips_dict.items():
        pos=pos-1
        forward_mappings[pos]=clip_data[2]
        reverse_mappings[pos]=clip_data[3]
    return forward_mappings,reverse_mappings

def gap_coverage(pileup,l):
    #the nucleotides are stored in the first 4 rows of the pileup
    forward=pileup[0]
    reverse=pileup[1]
    forward_coverage=np.zeros(l)
    reverse_coverage=np.zeros(l)
    for nuc_i,nuc in enumerate(forward):
        for pos,val in enumerate(nuc):
            forward_coverage[pos]+=forward[nuc_i,pos]
            reverse_coverage[pos]+=reverse[nuc_i,pos]
    return forward_coverage,reverse_coverage

def sum_forward_reverse(fwd,rev):
    #takes forward and reverse counts, gives total counts
    total=np.zeros(np.shape(fwd))
    for pos,val in enumerate(fwd):
        total[pos]=fwd[pos]+rev[pos]
    return total

def threshold_on_value_of_array(to_filter, array, t):
    #takes three arrays to filter on the basis of three values of another array
    output_tris=([],[],[])
    check=True
    for pos,val in enumerate(to_filter[0]):
        for direction,vector in enumerate(to_filter):
            if array[direction][pos]<t:
                check=False
        if check:
            for i,v in enumerate(output_tris):
                output_tris[i].append(to_filter[i][pos])
        check=True
    return output_tris

def generate_frequencies(pileup,reference,clips_dict,insertions_dict,t1,t2):

    l=np.shape(pileup)[2]
    
    arrays={}
    fwd,rev=clips(clips_dict,l)
    arrays['clips']=(fwd,rev)
    fwd,rev=insertions(insertions_dict,l)
    arrays['insertions']=(fwd,rev)
    fwd,rev=gaps(pileup,l)
    arrays['gaps']=(fwd,rev)

    forward_coverage, reverse_coverage = coverage(pileup,l)
    tot_coverage = sum_forward_reverse(forward_coverage,reverse_coverage)
    coverage_array=(forward_coverage,reverse_coverage,tot_coverage)

    forward_maps, reverse_maps = get_total_mappings(clips_dict,l)
    tot_maps = sum_forward_reverse(forward_maps,reverse_maps)
    maps_array=(forward_maps,reverse_maps,tot_maps)

    forward_gap_coverage, reverse_gap_coverage = gap_coverage(pileup,l)
    tot_gap_coverage = sum_forward_reverse(forward_gap_coverage,reverse_gap_coverage)
    gap_coverage_array=(forward_gap_coverage,reverse_gap_coverage,tot_gap_coverage)
    
    for key,val in arrays.items():
        fwd,rev=val
        tot=sum_forward_reverse(fwd,rev)
        array=[fwd,rev,tot]
        for i,direction in enumerate(array):
            if key=='clips':
                array[i]=array[i]/maps_array[i]
            if key=='gaps':
                array[i]=array[i]/gap_coverage_array[i]
            else:
                array[i]=array[i]/coverage_array[i]
        arrays[key]=array

    fncf, rncf, tncf = ncf(pileup,reference,l)
    arrays['ncf'] = (fncf, rncf, tncf)
    
    for key,val in arrays.items():
        if key=='clips':
            arrays[key]=threshold_on_value_of_array(val,maps_array,t1)
        else:
            arrays[key]=threshold_on_value_of_array(val,coverage_array,t2)
    
    return arrays