#!/bin/bash

#SBATCH --job-name=test                   #This is the name of your job
#SBATCH --cpus-per-task=1                  #This is the number of cores reserved
#SBATCH --mem-per-cpu=1G              #This is the memory reserved per core.
#Total memory reserved: 1GB

#SBATCH --time=00:30:00        #This is the time that your task will run
#SBATCH --qos=30min           #You will run in this queue

# Paths to STDOUT or STDERR files should be absolute or relative to current working directory
#SBATCH --output=test/stdout.txt     #These are the STDOUT and STDERR files
#SBATCH --error=test/stderr.txt

#This job runs from the current working directory


#Remember:
#The variable $TMPDIR points to the local hard disks in the computing nodes.
#The variable $HOME points to your home directory.
#The variable $SLURM_JOBID stores the ID number of your job.


#load your required modules below
ml Python

#export your required environment variables below

#add your command lines below
mamba activate phages_genome_assembly
python python_script.py