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
    parser.add_argument("--timesteps", help="file names to read, separated by a comma")

    args = parser.parse_args()
    in_dir=args.in_dir
    timesteps=args.timesteps
    '''
    in_dir='scores/EC2D2/new_chemistry'
    timesteps={'new_chemistry':0,'1':0,'3':0,'5':0}
    ##!!!design problem!!!!!!!!

    for step in timesteps.keys():
        file=f'{in_dir}/{step}.csv'
        timesteps[step]=pd.read_csv(file,index_col=0)

    #timesteps is a dictionary in which the key is the timepoint, the value is a dataframe with the data of that timepoint

    parameters_timespan={}
    for parameter in timesteps['new_chemistry']:######!!!!!!!!!!!!design problem!!!!!!!!!!!!!!!!
        parameters_timespan[parameter]=pd.DataFrame()
        for i,timestep in enumerate(timesteps.keys()):
            timestep_data=timesteps[timestep][parameter]
            parameters_timespan[parameter].insert(i,timestep,timestep_data,True)

    '''
    ###
    #plot the frequency distributions of each timestep
    ###

    for parameter,timepoints_data in parameters_timespan.items():
        fig, axs = plt.subplots(4,figsize=(10,10),sharex=True)
        fig.suptitle(parameter)
        for i,timepoint in enumerate(timepoints_data):
            to_plot=[]
            for frequency in timepoints_data[timepoint]:
                if not(np.isnan(frequency)):
                    to_plot.append(frequency)
            axs[i].hist(to_plot,bins=200)
            axs[i].set_title(timepoint)
            axs[i].set_yscale('log')
        plt.show()

    '''
    ###
    #plot the highest variation sites in the genome over time
    ###

    for parameter,timepoints_data in parameters_timespan.items():
        
        fig, axs = plt.subplots(4,figsize=(10,10),sharex=True)
        fig.suptitle(parameter)
        for i,timepoint in enumerate(timepoints_data):
            to_plot=[]
            for frequency in timepoints_data[timepoint]:
                if not(np.isnan(frequency)):
                    to_plot.append(frequency)
            axs[i].hist(to_plot,bins=200)
            axs[i].set_title(timepoint)
            axs[i].set_yscale('log')

        #if parameter == 'ncf':
        score_functions=[]
        for row in timepoints_data.itertuples():
    
            if not(np.isnan(row[1:]).any()) and row[0]>200 and row[0]<120000:
                #score_function=np.std(row[1:])
                #score_function=np.nanmax(row[1:])-np.nanmin(row[1:])
                score_function=row[-1]-row[1]

                score_functions.append(score_function)

            else:
                score_functions.append(np.nan)

        series_score_functions=pd.Series(score_functions)
        significant_sites=series_score_functions.nlargest(n=10)
        
        print(significant_sites)

        to_plot={}
        for site in significant_sites.index:
            for row in timepoints_data.itertuples():
                if row[0]==site:
                    to_plot[site]=row[1:]
        
        frquencies_on_time=plt.figure()
        timesteps=[0,1,3,5]####!!!!!!!!!!!!!!!!!!!!!!!!!!!design problem!!!!!!!!!!!!!!!!!!!
        for site,linepoints in to_plot.items():
            plt.plot(timesteps,linepoints)
            plt.title(parameter)
        plt.legend(to_plot.keys())
        plt.show()