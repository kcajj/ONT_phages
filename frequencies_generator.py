import numpy as np
from pileup_plots import coverage,clips,insertions,gaps

def get_entropy(obs):
    n=sum(obs)
    entropy=0
    for observation in obs:
        entropy-=(observation/n)*np.log((observation/n))
    return entropy

def ncf(pileup, reference, l):
    forward=pileup[0]
    reverse=pileup[1]
    alphabet='ACGT-N'
    forward_non_consensus_freq=np.zeros(l)
    reverse_non_consensus_freq=np.zeros(l)
    non_consensus_freq=np.zeros(l)

    for pos,ref_nuc in enumerate(reference):
        #forward_non_consensus=[0,0,0,0]
        #reverse_non_consensus=[0,0,0,0]
        #non_consensus=[0,0,0,0]
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
            if (not nuc==ref_nuc) and i_nuc<4:
                forward_non_consensus+=forward[i_nuc][pos]
                reverse_non_consensus+=reverse[i_nuc][pos]
                non_consensus+=forward[i_nuc][pos]+reverse[i_nuc][pos]
        
        #insert a measure of entropy, if entropy in the site is high, we trust less the measure.
        #if entropy is low we weight more the observed frequency.
        #merge the 4 non consensus measures before computing the frequency
        #forward_non_consensus=sum(forward_non_consensus)/get_entropy(forward_non_consensus)
        #reverse_non_consensus=sum(reverse_non_consensus)/get_entropy(reverse_non_consensus)
        #non_consensus=sum(non_consensus)/get_entropy(non_consensus)

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
    for pos,val in enumerate(array[0]):
        for direction,vector in enumerate(array):
            if vector[pos]<t:
                for v in to_filter:
                    v[pos]=np.nan
                    #to_filter[2][pos]=np.nan
                break
    return to_filter

def threshold_on_value_of_delta(to_filter, t):
    for pos,val in enumerate(to_filter[0]):
        if abs(to_filter[0][pos]-to_filter[1][pos])>t:
            for vector in to_filter:
                vector[pos]=np.nan
    return to_filter

def generate_frequencies(pileup,reference,clips_dict,insertions_dict,clips_threshold,gap_cov_threshold,cov_threshold,delta_fr_threshold):

    l=np.shape(pileup)[2]
    
    arrays={}
    fwd,rev=clips(clips_dict,l)
    arrays['clips']=[fwd,rev]
    fwd,rev=insertions(insertions_dict,l)
    arrays['insertions']=[fwd,rev]
    fwd,rev=gaps(pileup,l)
    arrays['gaps']=[fwd,rev]

    forward_coverage, reverse_coverage = coverage(pileup,l)
    tot_coverage = sum_forward_reverse(forward_coverage,reverse_coverage)
    coverage_array=[forward_coverage,reverse_coverage,tot_coverage]

    forward_maps, reverse_maps = get_total_mappings(clips_dict,l)
    tot_maps = sum_forward_reverse(forward_maps,reverse_maps)
    maps_array=[forward_maps,reverse_maps,tot_maps]

    forward_gap_coverage, reverse_gap_coverage = gap_coverage(pileup,l)
    tot_gap_coverage = sum_forward_reverse(forward_gap_coverage,reverse_gap_coverage)
    gap_coverage_array=[forward_gap_coverage,reverse_gap_coverage,tot_gap_coverage]
    
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
    arrays['non_consensus_frequency'] = [fncf, rncf, tncf]
    
    #arrays has as many keys as the parameters, each parameters has 3 vectors

    for key,three_vect in arrays.items():
        if key=='clips':
            arrays[key]=threshold_on_value_of_array(three_vect,maps_array,clips_threshold)
        if key=='gaps':
            arrays[key]=threshold_on_value_of_array(three_vect,gap_coverage_array,gap_cov_threshold)
        else:
            arrays[key]=threshold_on_value_of_array(three_vect,coverage_array,cov_threshold)

    for key,three_vect in arrays.items():
        arrays[key]=threshold_on_value_of_delta(three_vect,delta_fr_threshold)

    for key,three_vect in arrays.items():
        arrays[key]=arrays[key][2]
        
    return arrays