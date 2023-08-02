import os
import matplotlib.pyplot as plt

def saveplot(x,y1,y2,name):
    figure=plt.figure(figsize=(25,4))
    plt.plot(x,y1,y2)
    plt.legend(['forward','reverse'])
    plt.title(name)
    figure.savefig(f'results_pileup_plots/EC2D2/{name}.png')