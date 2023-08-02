import gzip
from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt

len_dict={}

with gzip.open("EC2D2_new_chemistry.fastq.gz", "rt") as handle:
    for record in SeqIO.parse(handle, "fastq"):
        l=len(record.seq)
        if l not in len_dict.keys():
            len_dict[l]=1
        else:
            len_dict[l]+=1

print('the total number of reads is:', sum(len_dict.values()))
max_len=max(len_dict.keys())

b=np.linspace(0, max_len+1, max_len+1)
len_distr=np.zeros(max_len+1)
for pos,val in len_dict.items():
    len_distr[pos]+=val
len_distr=np.convolve(len_distr, np.ones(50), mode='valid')

plt.plot(b,len_distr)
plt.show()