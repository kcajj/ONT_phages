#!/bin/bash

#SBATCH --job-name=EC2D2_nc_assembly                   #This is the name of your job
#SBATCH --cpus-per-task=4                  #This is the number of cores reserved
#SBATCH --mem-per-cpu=16G              #This is the memory reserved per core.
#Total memory reserved: 64GB

#SBATCH --time=00:30:00        #This is the time that your task will run
#SBATCH --qos=30min           #You will run in this queue

# Paths to STDOUT or STDERR files should be absolute or relative to current working directory
#SBATCH --output=stdout.txt     #These are the STDOUT and STDERR files
#SBATCH --error=stderr.txt

#This job runs from the current working directory


#Remember:
#The variable $TMPDIR points to the local hard disks in the computing nodes.
#The variable $HOME points to your home directory.
#The variable $SLURM_JOBID stores the ID number of your job.


#load your required modules below
ml Python

#export your required environment variables below
bash genome_assembly_script.sh