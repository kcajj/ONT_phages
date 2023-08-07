import os
import matplotlib.pyplot as plt
import numpy as np

def convolution(array,k):
    return np.convolve(array,np.ones(k),mode='valid')

def saveplot(y1,y2,k,folder,name):
    conv_y1=convolution(y1,k)/k
    conv_y2=convolution(y2,k)/k
    l=np.shape(conv_y1)[0]
    x=np.linspace(0,l,l)
    figure=plt.figure(figsize=(25,4))
    plt.plot(x,conv_y1,conv_y2)
    plt.legend(['forward','reverse'])
    plt.suptitle(name)
    plt.ylabel(str('average '+ name +' per base'))
    plt.xlabel('bp')
    plt.title(str(folder+', using '+str(k)+' as convolution window'), fontsize=9)
    try:
        os.makedirs(folder)
    except FileExistsError:
        pass
    figure.savefig(f'{folder}/{name}.png')