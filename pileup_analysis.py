import numpy as np
import matplotlib.pyplot as plt

from handle_npz_pkl import extract_seq, extract_npz, extract_pkl
from pileup_plots import coverage,non_consensus_frequency,clips,gaps
from plot_storage import saveplot

if __name__ == "__main__":
    #reads-assembly alignment
    sample='EC2D2'
    ref_file=f'results_genome_assembly/{sample}/assembly.fasta'
    pileup_file=f'results_pileup/{sample}/allele_counts_reads_assembly.npz'
    #pileup_file=f'results_pileup/{sample}/allele_counts.npz'
    clips_file=f'results_pileup/{sample}/clips_reads_assembly.pkl.gz'
    #clips_file=f'results_pileup/{sample}/clips.pkl.gz'
    gaps_file=f'results_pileup/{sample}/insertions_reads_assembly.pkl.gz'
    #gaps_file=f'results_pileup/{sample}/insertions.pkl.gz'

    pileup=extract_npz(pileup_file,'arr_0')
    reference=extract_seq(ref_file)
    clips_dict=extract_pkl(clips_file,'count')
    gaps_dict=extract_pkl(gaps_file)

    x,y1,y2=coverage(pileup)
    saveplot(x,y1,y2,sample,'coverage')
    
    x,y1,y2=non_consensus_frequency(pileup,reference,100)
    saveplot(x,y1,y2,sample,'non_consensus_assembly')

    x,y1,y2=clips(pileup,clips_dict,100)
    saveplot(x,y1,y2,sample,'clips')

    x,y1,y2=gaps(pileup,gaps_dict,1000)
    saveplot(x,y1,y2,sample,'gaps')
