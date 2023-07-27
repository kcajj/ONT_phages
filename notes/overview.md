# ONT data analysis

overall steps:
1. consensus assembly
2. map reads to the assembly

tools to know:
- conda: https://docs.conda.io/en/latest/miniconda.html https://docs.conda.io/en/latest/
- mamba:https://mamba.readthedocs.io/en/latest/
- tmux: https://tmuxcheatsheet.com/
- slurm: https://wiki.biozentrum.unibas.ch/display/scicore/SLURM+user+guide


useful things to know about the cluster:
- htop: lists the resources of the current machine (-u username to see the processes run by me)
- we have a shared folder in the cluster: /scicore/home/neher/GROUP. in this directory there is the data that we will use for this project: GROUP/data/Giacomo_analysis/
- squeue: lists the queue of slurm (-u username to see my jobs)
- srun: runs an interactive shell. basic command to run it: srun --qos=6hours --cpus-per-task=2 -mem=8G --pty bash
- i only have internet in my folder on the cluster, i do not have internet during job execution

## consensus assembly

tools:
- miniasm: https://github.com/lh3/miniasm (minipolish? https://github.com/rrwick/Minipolish)
- flye: https://github.com/fenderglass/Flye