def extract_npz(path, array_name):
    import numpy as np
    file=np.load(path)
    array=file[array_name]
    return array

def extract_pkl(path, field=''):
    import gzip
    import pickle
    with gzip.open(path) as f:
        file = pickle.load(f)
        if field=='':
            return file
        dictionary = file[field]
    return dictionary

def extract_seq(path):
    from Bio import SeqIO
    return SeqIO.read(path, 'fasta').seq