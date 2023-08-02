import numpy as np
import matplotlib.pyplot as plt

def make_plot(counts,clips):
    allele_counts=np.load(counts)
    print(allele_counts.files)
    array=allele_counts['arr_0']

    forward=array[0]
    reverse=array[1]

    b=np.linspace(0,np.shape(forward)[1],np.shape(forward)[1])

    coverage=np.zeros(np.shape(forward)[1])

    for nuc in forward:
        for pos in range(len(nuc)):
            coverage[pos]+=nuc[pos]

    coverage_plot=plt.figure(figsize=[25,4])
    plt.plot(b,coverage)

    import gzip
    import pickle

    clips_position=np.zeros(np.shape(forward)[1])

    with gzip.open(clips, 'rb') as f:
        clips = pickle.load(f)

    print(clips.keys())
    count=clips["count"]

    for clip in count.keys():
        clips_position[clip-1]=count[clip][2]

    clip_plot=plt.figure(figsize=[25,4])
    plt.plot(b, clips_position)

    plt.show()

if __name__ == "__main__":
    #reads-assembly alignment
    allele_counts_reads_assembly='results_read_mapping/EC2D2/allele_counts_reads_assembly.npz'
    clips_reads_assembly='results_read_mapping/EC2D2/clips_reads_assembly.pkl.gz'
    make_plot(allele_counts_reads_assembly,clips_reads_assembly)
    allele_counts_reads_reference='results_read_mapping/EC2D2/allele_counts_reads_reference.npz'
    clips_reads_reference='results_read_mapping/EC2D2/clips_reads_reference.pkl.gz'
    make_plot(allele_counts_reads_reference,clips_reads_reference)
