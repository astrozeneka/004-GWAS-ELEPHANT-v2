#!/bin/bash
#SBATCH -p compute
#SBATCH -N 1 -c 1
#SBATCH -t 01:00:00
#SBATCH -J gemma_wang2021
#SBATCH -A proj5034

source ~/.bashrc

export PLINK_RESULT_DIRECTORY="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/plink_ema_hair"

ldak --cut-weights "./" \
  --bfile "${PLINK_RESULT_DIRECTORY}/snp.hair"