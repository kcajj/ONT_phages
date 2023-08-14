import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from handle_npz_pkl import extract_seq, extract_npz, extract_pkl
from frequencies_generator import generate_frequencies
from parameters_distribution import parameters_distributions

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
    out_file='scores/EC2D2/new_chemistry/new_chemistry.csv'
    ref_file='results/EC2D2/assemblies/new_chemistry.fasta'
    
    pileup_file=f'{in_folder}/allele_counts.npz'
    clips_file=f'{in_folder}/clips.pkl.gz'
    insertions_file=f'{in_folder}/insertions.pkl.gz'
    
    pileup=extract_npz(pileup_file,'arr_0')
    reference=extract_seq(ref_file)
    clips_dict=extract_pkl(clips_file,'count')
    insertions_dict=extract_pkl(insertions_file)

    clips_threshold=10
    gap_cov_threshold=100
    cov_threshold=100
    delta_fr_threshold=0.1

    #parameters_distributions(pileup,reference,clips_dict,insertions_dict,clips_threshold,gap_cov_threshold,cov_threshold,delta_fr_threshold)
    
    frequencies=generate_frequencies(pileup,reference,clips_dict,insertions_dict,clips_threshold,gap_cov_threshold,cov_threshold,delta_fr_threshold)
    
    to_store=pd.DataFrame(frequencies)
    to_store.to_csv(out_file)