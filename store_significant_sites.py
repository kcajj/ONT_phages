import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

def store_sites(dictionary_input,name,out_dir):
    try:
        os.makedirs(out_dir)
    except FileExistsError:
        pass
    with open(f'{out_dir}/{name}.pkl', 'wb') as fp:
        pickle.dump(dictionary_input, fp)