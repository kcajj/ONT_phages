import gzip
from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt

len_dict={}

qual_dict={}
for n in range(100):
    qual_dict[n]=0

with gzip.open("data/nanopore/EC2D2_new_chemistry.fastq.gz", "rt") as handle:
    for record in SeqIO.parse(handle, "fastq"):
        l=len(record.seq)
        if l not in len_dict.keys():
            len_dict[l]=1
        else:
            len_dict[l]+=1
        q=record.format('qual')
        q_string=q.replace('\n',' ')
        q_list=q_string.split(' ')[8:-1]
        for nuc_qscore in q_list:
            qual_dict[int(nuc_qscore)]+=1

print('the total number of reads is:', sum(len_dict.values()))
max_len=max(len_dict.keys())

b=np.linspace(0, max_len, max_len)
len_distr=np.zeros(max_len)
for pos,val in len_dict.items():
    len_distr[pos-1]+=val

len_distr=np.convolve(len_distr, np.ones(100), mode='same')

plt.plot(b,len_distr)

plt.show()

x=np.linspace(0,100,100)
qual_distr=[]
for q in qual_dict.values():
    qual_distr.append(q)

plt.plot(x,qual_distr)
plt.show()