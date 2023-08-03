import os
import matplotlib.pyplot as plt

def saveplot(x,y1,y2,folder,name):
    figure=plt.figure(figsize=(25,4))
    plt.plot(x,y1,y2)
    plt.legend(['forward','reverse'])
    plt.title(name)
    try:
        os.makedirs(folder)
    except FileExistsError:
        pass
    figure.savefig(f'{folder}/{name}.png')