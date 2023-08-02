import numpy as np
import matplotlib.pyplot as plt

allele_counts=np.load('results_read_mapping/EC2D2/allele_counts_reads_assembly.npz')
print(allele_counts.files)
array=allele_counts['arr_0']

forward=array[0]
reverse=array[1]

b=np.linspace(0,np.shape(forward)[1],np.shape(forward)[1])

coverage=np.zeros(np.shape(forward)[1])

for nuc in forward:
    for pos in range(len(nuc)):
        coverage[pos]+=nuc[pos]

coverage_plot=plt.figure()
plt.plot(b,coverage)

import gzip
import pickle

clips_position=np.zeros(np.shape(forward)[1])

with gzip.open('results_read_mapping/EC2D2/clips_reads_assembly.pkl.gz', 'rb') as f:
    clips = pickle.load(f)

print(clips.keys())
count=clips["count"]

for clip in count.keys():
    clips_position[clip-1]=count[clip][2]

clip_plot=plt.figure()
plt.plot(b, clips_position)

plt.show()