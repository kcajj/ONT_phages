# ONT data analysis

what are we working on:
- [phage evolution](phages.md)
- [pangraph](pangraph.md)

steps that i have to do:
1. [consensus assembly](note_1.md)
2. map reads to the assembly

## general introduction to high power computing

tools to know:
- git
- conda: https://docs.conda.io/en/latest/
- mamba:https://mamba.readthedocs.io/en/latest/
- tmux: https://tmuxcheatsheet.com/
- slurm: https://wiki.biozentrum.unibas.ch/display/scicore/SLURM+user+guide

## cluster
useful things to know about the cluster:
- htop: lists the resources of the current machine (-u username to see the processes run by me)
- we have a shared folder in the cluster: /scicore/home/neher/GROUP. in this directory there is the data that we will use for this project: GROUP/data/Giacomo_analysis/
- squeue: lists the queue of slurm (-u username to see my jobs)
- srun: runs an interactive shell, it's like a job but it is interactive. basic command to run it: srun --qos=6hours --cpus-per-task=2 --mem=8G --pty bash
- i only have internet in my folder on the cluster, i do not have internet during job execution
- scancel <jobID> or scancel -u <username>

cluster setup (in case i will have to do it again in the future):
- login: ssh username@server address (login.scicore.unibas.ch)
- login without password: ssh-keygen, ssh-copy-id -i ~/.ssh/id_rsa.pub user@server
- set the server as system folder: add to ".bashrc": alias mount_scicore="sshfs -o reconnect -o follow_symlinks user@login-transfer.server:/server/folder /system/folder. (the system folder has to exist already)
- connect vscode to the cluster: bottom left corner, click on open a remote window, search for ssh, add new ssh host

## git
base notions on git:
- git config: set up username and email
- git init: to make a folder a git repo
- git status: to see the status of the repo
- to commit: git add files, git commit -m "message"
- git log: history of commits
- to go back to a previous commit: git checkout commit_hash or git checkout branch
- git branch: list branches
- git merge branch-to-merge
- connect to a repo: git remote add origin repo-link
- set target branch to main: git branch -M main
- push to the cloud: git push -u origin main4
- git pull
- clone a repo with ssh access: git clone sshlink
- git ignore: .gitignore is a file containing in each line the relative path of the elements that are not considered in git sync

[github cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)

## conda
basic notions on conda:
- conda create -n name python=3.11
- conda env list
- conda activate ./folder
- inside a conda environment: conda install whatever
- conda remove --name myenv --all
- conda env export > environment.yml (conda env create -f environment.yml, conda env update --name myenv --file environment.yml  --prune)

[conda cheat sheet](/images/conda-4.14.pdf)

mamba has the same commands. conda and mamba work on the same environments, they are kinda shared. we will always work with mamba becuase it is faster.

## slurm

general structure of a slurm script:

#!/bin/bash

options:
    --job-name
    --cpus-per-task
    --ntasks
    --mem-per-cpu
    --time
    --qos           choose the qos wisely, overestimate!
    --output
    --error

modules

commands

the file has to be savesd in .sh, then submitted to the queue with "sbatch script.sh".

actually [this site](https://scriptgen.scicore.unibas.ch/pages/generate_slurm.html) builds slurm scripts for you! i may use this at the beginning

### example
#!/bin/bash                 
#The previous line is mandatory
 
#SBATCH --job-name=myrun     #Name of your job
#SBATCH --cpus-per-task=1    #Number of cores to reserve
#SBATCH --mem-per-cpu=1G     #Amount of RAM/core to reserve
#SBATCH --time=06:00:00      #Maximum allocated time
#SBATCH --qos=6hours         #Selected queue to allocate your job
#SBATCH --output=myrun.o%j   #Path and name to the file for the STDOUT
#SBATCH --error=myrun.e%j    #Path and name to the file for the STDERR
 
ml Python                    #Load required modules
python my_script.py inputdata.txt    #Execute your command(s)

## general commonsense pipeline to use the cluster
1. connect to the cluster
2. activate tmux!!! super important, first thing to do.
3. run the script (inside the script it's like a new terminal window is running, i have to write each command)

DO NOT FORGET ANY OPEN TMUX SESSION IF THEY ARE NOT NECESSARY