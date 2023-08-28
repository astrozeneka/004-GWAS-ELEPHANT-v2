#!/bin/bash
#SBATCH -p compute
#SBATCH -N 1 -c 1
#SBATCH -t 01:00:00
#SBATCH -J gemma_wang2021
#SBATCH -A proj5034

export PLINK_RESULT_DIRECTORY="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/plink_ema_hair"
export PHENO_FILE="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/gemma_hair/pheno.txt"
# GEMMA OUTPUT DIRECTORY คือ ./output

gemma -bfile "${PLINK_RESULT_DIRECTORY}/snp.hair" -k kinship -lmm 1 -p "${PHENO_FILE}" -o output

# แลังจากนี้ต้องรัน awk อีกที
# awk < thin.in '{print $1,1}' > weights.thin

# แล้วก็ ldak
# ldak --calc-kins-direct kinship --bfile input --weights weights.thin --power -.25
