import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import random

if __name__ == "__main__":

    phages=['EC2D2','EM11','EM60']

    for phage in phages:
        in_dir=f'scores/{phage}/new_chemistry'
        timesteps={'new_chemistry':0,'1':0,'3':0,'5':0}
        
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

        ###
        #plot the highest variation sites in the genome over time
        ###

        for parameter,timepoints_data in parameters_timespan.items():

            ###
            #plot the frequency distributions of each timestep
            ###
            fig, axs = plt.subplots(4,figsize=(10,10),sharex=True)
            fig.suptitle(parameter)
            for i,timepoint in enumerate(timepoints_data):
                to_plot=[]
                for frequency in timepoints_data[timepoint]:
                    if not(np.isnan(frequency)) and not(np.isinf(frequency)):
                        to_plot.append(frequency)
                axs[i].hist(to_plot,bins=200)
                axs[i].set_title(timepoint)
                axs[i].set_yscale('log')

            fig.savefig(f'plots/time_analysis/{phage}/distribution_{parameter}.png')
            plt.close()

            #if parameter == 'ncf':
            score_functions=[]
            for row in timepoints_data.itertuples():
        
                if not(np.isnan(row[1:]).any()):
                    #score_function=np.std(row[1:])
                    #score_function=np.nanmax(row[1:])-np.nanmin(row[1:])
                    score_function=row[-1]-row[1]

                    score_functions.append(score_function)

                else:
                    score_functions.append(np.nan)

            series_score_functions=pd.Series(score_functions)
            significant_sites=series_score_functions.nlargest(n=10)
            
            to_plot={}
            for site in significant_sites.index:
                for row in timepoints_data.itertuples():
                    if row[0]==site:
                        to_plot[site]=row[1:]
            
            frequencies_on_time=plt.figure()
            timesteps=[0,1,3,5]####!!!!!!!!!!!!!!!!!!!!!!!!!!!design problem!!!!!!!!!!!!!!!!!!!
            for site,linepoints in to_plot.items():
                plt.plot(timesteps,linepoints)
                plt.title(parameter)
            plt.legend(to_plot.keys())
            
            frequencies_on_time.savefig(f'plots/time_analysis/{phage}/time_dynamics_{parameter}.png')
            plt.close()