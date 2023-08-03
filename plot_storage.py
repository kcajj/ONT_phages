import os
import matplotlib.pyplot as plt

def saveplot(x,y1,y2,sample,name):
    figure=plt.figure(figsize=(25,4))
    plt.plot(x,y1,y2)
    plt.legend(['forward','reverse'])
    plt.title(name)
    os.mkdir(f'results_pileup_plots/{sample}')
    figure.savefig(f'results_pileup_plots/{sample}/{name}.png')