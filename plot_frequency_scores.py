import numpy as np
import matplotlib.pyplot as plt

from handle_npz_pkl import extract_seq, extract_npz, extract_pkl
from frequencies_generator import generate_frequencies

import pickle

def store_sites(dictionary_input,out_file):
    with open(out_file, 'wb') as fp:
        pickle.dump(dictionary_input, fp)

if __name__ == "__main__":
    '''
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
    in_folder='results/EC2D2/pileup/new_chemistry/new_chemistry'
    out_file='significant_sites/EC2D2/new_chemistry.pkl'
    ref_file='results/EC2D2/assemblies/new_chemistry.fasta'
    
    pileup_file=f'{in_folder}/allele_counts.npz'
    clips_file=f'{in_folder}/clips.pkl.gz'
    insertions_file=f'{in_folder}/insertions.pkl.gz'
    
    pileup=extract_npz(pileup_file,'arr_0')
    reference=extract_seq(ref_file)
    clips_dict=extract_pkl(clips_file,'count')
    insertions_dict=extract_pkl(insertions_file)

    t1=3
    t2=10
    
    frequencies=generate_frequencies(pileup,reference,clips_dict,insertions_dict,t1,t2)

    #check the counter of read mapping position in build_pileup script, saved in the clips dictionary

    for key,val in frequencies.items():
        for vector in val:
            for element in vector:
                if np.isnan(element):
                    element=0
        plt.hist(val[2],bins=200)
        plt.title(key)
        plt.yscale('log')
        plt.show()
        
    significant_sites={}
    for key in frequencies.keys():
        significant_sites[key]=[]

    t3=0.7 #threshold on score
    t4=0.1

    for key,val in frequencies.items():
        for pos,score in enumerate(val[2]): #run along the total scores
            if score>t3:
                if val[0][pos]-val[1][pos]<t4:
                    significant_sites[key].append((score,pos))

    #normalise for base frequences
    for i,v in significant_sites.items():
        print(i,v)
        
    store_sites(significant_sites,out_file)