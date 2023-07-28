# ONT data analysis

overall steps:
1. consensus assembly
2. map reads to the assembly

tools to know:
- conda: https://docs.conda.io/en/latest/
- mamba:https://mamba.readthedocs.io/en/latest/
- tmux: https://tmuxcheatsheet.com/
- slurm: https://wiki.biozentrum.unibas.ch/display/scicore/SLURM+user+guide


useful things to know about the cluster:
- htop: lists the resources of the current machine (-u username to see the processes run by me)
- we have a shared folder in the cluster: /scicore/home/neher/GROUP. in this directory there is the data that we will use for this project: GROUP/data/Giacomo_analysis/
- squeue: lists the queue of slurm (-u username to see my jobs)
- srun: runs an interactive shell, it's like a job but it is interactive. basic command to run it: srun --qos=6hours --cpus-per-task=2 -mem=8G --pty bash
- i only have internet in my folder on the cluster, i do not have internet during job execution

cluster setup (in case i will have to do it again in the future):
- login: ssh username@server address (login.scicore.unibas.ch)
- login without password: ssh-keygen, ssh-copy-id -i ~/.ssh/id_rsa.pub user@server
- set the server as system folder: add to ".bashrc": alias mount_scicore="sshfs -o reconnect -o follow_symlinks user@login-transfer.server:/server/folder /system/folder. (the system folder has to exist already)

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
https://education.github.com/git-cheat-sheet-education.pdf
perplessità su git:
- come si tolgono delle righe da git config?
- sistemare la repo del west nile sul pc ubuntu

basic notions on conda:
- conda create

## consensus assembly

tools:
- miniasm: https://github.com/lh3/miniasm (minipolish? https://github.com/rrwick/Minipolish)
- flye: https://github.com/fenderglass/Flye