import numpy as np
import matplotlib.pyplot as plt

from handle_npz_pkl import extract_seq, extract_npz, extract_pkl
from pileup_plots import coverage,non_consensus_frequency,clips,gaps
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
    gaps_file=f'{in_folder}/insertions.pkl.gz'

    pileup=extract_npz(pileup_file,'arr_0')
    reference=extract_seq(ref_file)
    clips_dict=extract_pkl(clips_file,'count')
    gaps_dict=extract_pkl(gaps_file)

    x,y1,y2=coverage(pileup)
    saveplot(x,y1,y2,out_folder,'coverage')
    
    x,y1,y2=non_consensus_frequency(pileup,reference,100)
    saveplot(x,y1,y2,out_folder,'non_consensus_assembly')

    x,y1,y2=clips(pileup,clips_dict,100)
    saveplot(x,y1,y2,out_folder,'clips')

    x,y1,y2=gaps(pileup,gaps_dict,1000)
    saveplot(x,y1,y2,out_folder,'gaps')
