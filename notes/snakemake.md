# snakemake

config file:
genome-size:
  EC2D2: "0.150m"
  EM11: "0.140m"
  EM60: "0.140m"

local profile:
config.yaml:
use-conda: true
conda-frontend: 'mamba'
cores: 4
printshellcmds: true

cluster profile:
config.yaml:
cluster: "sbatch --time={cluster.time} --mem={cluster.mem} --cpus-per-task={cluster.n} --qos={cluster.qos}"
jobs: 20
jobscript: "cluster/slurm_submit.sh"
cluster-config: "cluster/cluster_config.json"
cluster-cancel: scancel
jobname: "{rulename}_{jobid}"
latency-wait: 90

use-conda: True
rerun-incomplete: True
conda-frontend: "mamba"

slurm_submit.sh:
#!/bin/sh

#SBATCH --output=log/%x.%j.out                 # where to store the output ( %j is the jobID )
#SBATCH --error=log/%x.%j.err                  # where to store error messages (%x is the jobname)

#Run .bashrc to initialize conda and julia
source $HOME/.bashrc

# Activate conda env
# conda activate (env-name)

{exec_job}

cluster_config.json:
{
    "__default__": {
        "time": "00:29:00",
        "qos": "30min",
        "n": 4,
        "mem": "8G"
}


run:
snakemake --profile local all