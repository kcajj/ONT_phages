import numpy as np

allele_counts=np.load('pileup_output/allele_counts.npz')
print(allele_counts.files)
array=allele_counts['arr_0']

print(np.shape(array))

forward=array[0]
reverse=array[1]

print(forward)

b=np.linspace(0,np.shape(forward)[1],np.shape(forward)[1])

y=np.zeros(np.shape(forward)[1])
