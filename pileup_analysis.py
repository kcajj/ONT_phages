import numpy as np
import matplotlib.pyplot as plt

from handle_npz_pkl import extract_seq, extract_npz, extract_pkl
from pileup_plots import coverage,non_consensus_frequency,clips,insertions,gaps
from plot_storage import saveplot

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="visualise pileup data",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--in_dir", help="directory containing pileup data")
    parser.add_argument("--ref", help="reference sequence")
    parser.add_argument("--out_dir", help="directory to save results")

    args = parser.parse_args()
    in_folder=args.in_dir
    out_folder=args.out_dir
    ref_file=args.ref

    pileup_file=f'{in_folder}/allele_counts.npz'
    clips_file=f'{in_folder}/clips.pkl.gz'
    insertions_file=f'{in_folder}/insertions.pkl.gz'

    k1=1000
    k2=10

    pileup=extract_npz(pileup_file,'arr_0')
    reference=extract_seq(ref_file)
    clips_dict=extract_pkl(clips_file,'count')
    insertions_dict=extract_pkl(insertions_file)

    l=np.shape(pileup)[2]

    y1,y2=coverage(pileup,l)
    saveplot(y1,y2,k1,out_folder,'coverage')
    
    y1,y2=non_consensus_frequency(pileup,reference,l)
    saveplot(y1,y2,k1,out_folder,'non_consensus_frequency')

    y1,y2=clips(clips_dict,l)
    saveplot(y1,y2,k2,out_folder,'clips')

    y1,y2=insertions(insertions_dict,l)
    saveplot(y1,y2,k2,out_folder,'insertions')

    y1,y2=gaps(pileup,l)
    saveplot(y1,y2,k2,out_folder,'gaps')