import pickle
import matplotlib.pyplot as plt

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
    #complete timespan is a list that has as many dictionaries as the number of timesteps, each contains as many dictionaries as the parameters

    for parameter in complete_timespan[0].keys():
        for timestep in complete_timespan:
            for dot in timestep[parameter]:
                
                plt.scatter(timestep_counter,dot[0],label=dot[1])

            timestep_counter+=1
        timestep_counter=0
        plt.show()