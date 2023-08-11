import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from handle_npz_pkl import extract_seq, extract_npz, extract_pkl
from frequencies_generator import generate_frequencies

if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser(
        description="visualise pileup data",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--in_dir", help="directory containing pileup data")
    parser.add_argument("--ref", help="reference sequence")
    parser.add_argument("--out", help="output dictionary file")

    args = parser.parse_args()
    in_folder=args.in_dir
    out_file=args.out
    ref_file=args.ref
    '''
    in_folder='results/EM11/pileup/new_chemistry/new_chemistry'
    out_file='scores/EM11/new_chemistry/new_chemistry.csv'
    ref_file='results/EM11/assemblies/new_chemistry.fasta'
    '''
    pileup_file=f'{in_folder}/allele_counts.npz'
    clips_file=f'{in_folder}/clips.pkl.gz'
    insertions_file=f'{in_folder}/insertions.pkl.gz'
    
    pileup=extract_npz(pileup_file,'arr_0')
    reference=extract_seq(ref_file)
    clips_dict=extract_pkl(clips_file,'count')
    insertions_dict=extract_pkl(insertions_file)

    clips_threshold=3
    gap_cov_threshold=50
    cov_threshold=50
    delta_fr_threshold=0.1
    
    frequencies=generate_frequencies(pileup,reference,clips_dict,insertions_dict,clips_threshold,gap_cov_threshold,cov_threshold,delta_fr_threshold)

    #check the counter of read mapping position in build_pileup script, saved in the clips dictionary

    for key,vector in frequencies.items():
        for element in vector:
            if np.isnan(element):
                element=0
        plt.hist(element,bins=200)
        plt.title(key)
        plt.yscale('log')
        #plt.show()

    to_store=pd.DataFrame(frequencies)
    to_store.to_csv(out_file)
    
    '''
    print(frequencies)

    significant_sites={}
    for key in frequencies.keys():
        significant_sites[key]=[]

    #score threshold for gaps should be higher because they are not affected by the quality filter

    score_threshold=0.5
    gaps_score_threshold=0.9
    delta_threshold=0.1

    for key,vector in frequencies.items():
        for pos,score in enumerate(vector): #run along the total scores
            if score>score_threshold:
                if key=='gaps':
                    if score>gaps_score_threshold:
                        significant_sites[key].append((score,pos))
                else:
                    if score>score_threshold:
                            significant_sites[key].append((score,pos))

    print(significant_sites)
    '''