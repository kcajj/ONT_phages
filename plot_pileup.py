import numpy as np
import matplotlib.pyplot as plt

def make_plot(counts,clips,direction):
    allele_counts=np.load(counts)
    print(allele_counts.files)
    array=allele_counts['arr_0']

    if direction=='forward':
        pileup=array[0]
    else:
        pileup=array[1]

    b=np.linspace(0,np.shape(pileup)[1],np.shape(pileup)[1])

    coverage=np.zeros(np.shape(pileup)[1])

    for nuc in pileup:
        for pos in range(len(nuc)):
            coverage[pos]+=nuc[pos]

    coverage_plot=plt.figure(figsize=[25,4])
    plt.plot(b,coverage)

    import gzip
    import pickle

    with gzip.open(clips, 'rb') as f:
        clips = pickle.load(f)

    clips_position=np.zeros(np.shape(pileup)[1])
    print(clips.keys())
    count=clips["count"]

    if direction=='forward':
        for clip in count.keys():
            clips_position[clip-1]=count[clip][2]
    else:
        for clip in count.keys():
            clips_position[clip-1]=count[clip][3]

    clip_plot=plt.figure(figsize=[25,4])
    plt.plot(b, clips_position)

    plt.show()

if __name__ == "__main__":
    #reads-assembly alignment
    allele_counts_reads_assembly='results_read_mapping/EC2D2/allele_counts_reads_assembly.npz'
    clips_reads_assembly='results_read_mapping/EC2D2/clips_reads_assembly.pkl.gz'
    make_plot(allele_counts_reads_assembly,clips_reads_assembly,'forward')
    make_plot(allele_counts_reads_assembly,clips_reads_assembly,'reverse')
    allele_counts_reads_reference='results_read_mapping/EC2D2/allele_counts_reads_reference.npz'
    clips_reads_reference='results_read_mapping/EC2D2/clips_reads_reference.pkl.gz'
    make_plot(allele_counts_reads_reference,clips_reads_reference,'forward')
    make_plot(allele_counts_reads_reference,clips_reads_reference,'reverse')
