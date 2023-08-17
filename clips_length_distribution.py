import numpy as np
import matplotlib.pyplot as plt

from handle_npz_pkl import extract_pkl

phages=['EC2D2','EM11','EM60']

for phage in phages:
    in_folder=f'results/{phage}/pileup/pileup_without_threshold/new_chemistry/new_chemistry'
    clips_file=f'{in_folder}/clips.pkl.gz'
    clips_dict=extract_pkl(clips_file,'len')

    len_distr=[]
    for clips in clips_dict.values():
        for clips_lens in clips.values():
            for clip_len in clips_lens:
                len_distr.append(clip_len)
    
    print(len(len_distr))
    print(sum(len_distr)/len(len_distr))

    minn=np.min(len_distr)
    maxx=np.max(len_distr)
    bins=np.logspace(np.log10(minn),np.log10(maxx),200)
    plt.hist(len_distr,bins=bins)
    plt.xscale('log')
    plt.yscale('log')
    line = plt.axvline(x = 270, color = 'r', label = '270 bp - threshold')
    plt.xlabel('clip length')
    plt.ylabel('number of reads')
    plt.show()