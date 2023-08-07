import numpy as np
import matplotlib.pyplot as plt

from handle_npz_pkl import extract_seq, extract_npz, extract_pkl
from pileup_plots import coverage,non_consensus_frequency,clips,gaps
from plot_storage import saveplot

folders=['pileup_and_plots_without_threshold/EC2D2/pileup',
         'pileup_and_plots_without_threshold/EM11/pileup',
         'pileup_and_plots_without_threshold/EM60/pileup']

for folder in folders:
    in_folder=folder
    #ref_file=args.ref

    clips_file=f'{in_folder}/clips.pkl.gz'
    clips_dict=extract_pkl(clips_file,'seqs')

    len_distr=[]
    for v in clips_dict.values():
        print(v)
        for seqs in v.values():
            for seq in seqs:
                l=len(seq)
                if l>1:
                    len_distr.append(l)

    m= max(len_distr)
    print(len(len_distr))
    print(sum(len_distr)/len(len_distr))
    print(m)
    minn=np.min(len_distr)
    maxx=np.max(len_distr)
    bins=np.logspace(np.log10(minn),np.log10(maxx),200)
    plt.hist(len_distr,bins=bins)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

