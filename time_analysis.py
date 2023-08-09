import pickle
import matplotlib.pyplot as plt
from collections import defaultdict
# Read dictionary pkl file
if __name__ == "__main__":
    '''
    import argparse

    parser = argparse.ArgumentParser(
        description="visualise pileup data",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--in_dir", help="directory with all the files from different timesteps")
    parser.add_argument("--timesteps", help="file names to parse, separated by a comma")

    args = parser.parse_args()
    in_dir=args.in_dir
    timesteps=args.timesteps
    '''
    in_dir='significant_sites/EC2D2'
    timesteps='0'
    timesteps=timesteps.split(',')

    complete_timespan=[]

    for step in timesteps:
        file=f'{in_dir}/{step}.pkl'
        with open(file, 'rb') as fp:
            significant_sites = pickle.load(fp)

            complete_timespan.append(significant_sites)

    timestep_counter=0
    lines_to_plot=defaultdict(list)
    #complete timespan is a list that has as many dictionaries as the number of timesteps, each contains as many dictionaries as the parameters

    for parameter in complete_timespan[0].keys():
        for timestep in complete_timespan:
            for dot in timestep[parameter]:
                
                lines_to_plot[dot[1]].append((timestep_counter,dot[0]))

            timestep_counter+=1
        timestep_counter=0
    
    for label,list_of_points in lines_to_plot.items():
        x=[]
        y=[]
        for p in list_of_points:
            
            x.append(p[0])
            y.append(p[1])
        plt.plot(x,y)
        plt.legend(label)

    plt.show()