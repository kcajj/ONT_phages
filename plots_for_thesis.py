import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import random
from convert_genome_coordinates import convert_coordinate

SMALL_SIZE = 12
MEDIUM_SIZE = 15
BIGGER_SIZE = 20

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

if __name__ == "__main__":

    phages=['EM11','EM60']

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

        for parameter,timepoints_data in parameters_timespan.items():
            if phage=="EM11" or phage=="EM60":
                if parameter=="clips" or parameter=="insertions": continue

            ###
            #plot the highest variation sites in the genome over time
            ###
            first_timepoint_threshold=0.15
            number_of_sites=20
            sites_to_keep=[]
            score_functions=[]            

            for row in timepoints_data.itertuples():
        
                if not(np.isnan(row[1:]).any()) and not(row[1]>first_timepoint_threshold):
                    #score_function=np.std(row[1:])
                    score_function=np.nanmax(row[1:])-np.nanmin(row[1:])
                    #score_function=row[-1]-row[1]

                    score_functions.append(score_function)

                else:
                    score_functions.append(np.nan)

            series_score_functions=pd.Series(score_functions)
            significant_sites=series_score_functions.nlargest(n=number_of_sites)

            significant_sites_with_data={}
            for site in significant_sites.index:
                for row in timepoints_data.itertuples():
                    if site==row[0]:
                        significant_sites_with_data[site]=row[1:]
            
            converted_significant_sites_with_data={}
            for significant_site,data in significant_sites_with_data.items():
                converted_site=convert_coordinate(phage,significant_site)
                converted_significant_sites_with_data[converted_site]=data

            to_plot={}
            for site,data in converted_significant_sites_with_data.items():
                if phage=="EM11":
                    if parameter=='non_consensus_frequency':
                        if site in [36588, 30397, 31963, 37242, 7328]:
                            to_plot[site]=data
                    elif parameter=="gaps":
                        if site in [43327, 43079]:
                            to_plot[site]=data
                        if site>38472 and site<38475:
                            to_plot["38472-38475"]=data
                        if site>47910 and site<47914:
                            to_plot["47910-47914"]=data
                        #to_plot[site]=data
                    else: to_plot[site]=data
                elif phage=="EM60":
                    if parameter=="non_consensus_frequency":
                        if site in [36619, 7696, 7695]:
                            to_plot[site]=data
                    elif parameter=="gaps":
                        if site in [28977, 44969]:
                            to_plot[site]=data
                        elif site>30532 and site<30540:
                            to_plot["30532-30540"]=data
                else: to_plot[site]=data
            
            frequencies_on_time=plt.figure()
            timesteps=[0,1,3,5]####!!!!!!!!!!!!!!!!!!!!!!!!!!!design problem!!!!!!!!!!!!!!!!!!!
            for site,linepoints in to_plot.items():
                plt.plot(timesteps,linepoints, linewidth=3)
                if  phage=="EM11":
                    phage_lab="bas51"
                else: phage_lab="bas54"
                if parameter=="non_consensus_frequency":
                    par_lab="non consensus frequency"
                else: par_lab=parameter
                plt.title(str('Phage '+phage_lab+' - '+par_lab))
                plt.xlabel('day')
                plt.ylabel('frequency')
                plt.ylim(0,1)
            plt.legend(to_plot.keys())

            frequencies_on_time.savefig(f'thesis/{phage}_time_{parameter}.png', dpi=600)
            plt.close()