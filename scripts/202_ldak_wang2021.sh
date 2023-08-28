#!/bin/bash
#SBATCH -p compute
#SBATCH -N 1 -c 1
#SBATCH -t 01:00:00
#SBATCH -J gemma_wang2021
#SBATCH -A proj5034

source ~/.bashrc

export PLINK_RESULT_DIRECTORY="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/plink_ema_hair"
export LD_IN="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/plink_ema_hair/LD.prune.in"

# ไม่เกียวกับ gemma
ldak --thin "${LD_IN}" --bfile "${PLINK_RESULT_DIRECTORY}/snp.hair" \
  --window-prune .98 --window-kb 100
