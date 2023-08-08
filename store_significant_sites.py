import numpy as np
import matplotlib.pyplot as plt
import pickle


def store_sites(dictionary_input,name,out_dir):
    with open(f'{out_dir}/{name}.pkl', 'wb') as fp:
            pickle.dump(dictionary_input, fp)