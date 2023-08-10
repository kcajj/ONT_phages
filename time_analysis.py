import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import random

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
    in_dir='scores/EC2D2/new_chemistry'
    timesteps={'new_chemistry':0,'1':0,'3':0,'5':0}
    ##!!!design problem!!!!!!!!

    complete_timespan=[]

    for step in timesteps.keys():
        file=f'{in_dir}/{step}.csv'
        timesteps[step]=pd.read_csv(file,index_col=0)

    #timesteps is a dictionary in which the key is the timepoint, the value is a dataframe with the data of that timepoint

    parameters_timespan={}
    for parameter in timesteps['new_chemistry']:######!!!!!!!!!!!!design problem!!!!!!!!!!!!!!!!
        parameters_timespan[parameter]=pd.DataFrame()
        for timestep in timesteps.keys():
            timestep_data=timesteps[timestep][parameter]
            parameters_timespan[parameter].insert(0,timestep,timestep_data,True)

    for parameter,timepoints_data in parameters_timespan.items():
        print(parameter)
        print(timepoints_data)
        score_functions=[]
        for row in timepoints_data.itertuples():


            score_function=np.std(row[1:])
            #score_function=np.nanmax(row[1:])-np.nanmin(row[1:])
            #score_function=row[-1]-row[1]


            score_functions.append(score_function)
        series_score_functions=pd.Series(score_functions)
        significant_sites=series_score_functions.nlargest(n=10)
        
        print(significant_sites)

        to_plot={}
        for site in significant_sites.index:
            for row in timepoints_data.itertuples():
                if row[0]==site:
                    to_plot[site]=row[1:]
        
        timesteps=[0,1,3,5]
        #timesteps=[0]
        print(to_plot)
        for site,linepoints in to_plot.items():
            plt.plot(timesteps,linepoints)
            plt.title(parameter)
        plt.legend(to_plot.keys())
        plt.show()

    '''
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
    '''