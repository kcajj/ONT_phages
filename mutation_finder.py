import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

from handle_npz_pkl import extract_seq, extract_npz, extract_pkl
from pileup_plots import coverage

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
            total+=forward_total+reverse_total
            if not nuc==ref_nuc:
                forward_non_consensus+=forward[i_nuc][pos]
                reverse_non_consensus+=reverse[i_nuc][pos]
                non_consensus+=forward_non_consensus+reverse_non_consensus

        forward_non_consensus_freq[pos]=forward_non_consensus/forward_total
        reverse_non_consensus_freq[pos]=reverse_non_consensus/reverse_total
        non_consensus_freq[pos]=non_consensus/total

    return forward_non_consensus_freq,reverse_non_consensus_freq,non_consensus_freq

if __name__ == "__main__":
    '''
    import argparse

    parser = argparse.ArgumentParser(
        description="visualise pileup data",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--pileup", help="directory containing pileup data")
    parser.add_argument("--ref", help="reference sequence")

    args = parser.parse_args()
    pileup_file=args.pileup
    ref_file=args.ref
    '''
    pileup_file='results/EC2D2/pileup/new_chemistry/new_chemistry/allele_counts.npz'
    ref_file='data/references/EC2D2_reference.fasta'
    pileup=extract_npz(pileup_file,'arr_0')
    reference=extract_seq(ref_file)

    l=np.shape(pileup)[2]
    fncf, rncf, tncf = ncf(pileup,reference,l)
    fcv, rcv = coverage(pileup,l)
    
    mutated_sites=defaultdict()

    for bp in range(l):
        if np.isnan(tncf[bp]):
            tncf[bp]=0
        print(tncf[bp])
        
        mutated_sites[round(tncf[bp],1)]+=1

    plt.plot(mutated_sites.keys(),mutated_sites.values())