#!/bin/bash
#SBATCH -p memory
#SBATCH -N 1 -c 96
#SBATCH -t 24:00:00
#SBATCH --mem=100GB
#SBATCH -J plink
#SBATCH -A proj5034

source ~/.bashrc
conda activate plink

VCF_FILE="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/plink_ema_hair_chr123/populations.snps.vcf"
PLINK_FILE="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/plink_ema_hair_chr123/snp.hair"
plink --make-bed --double-id -threads 96 \
  --vcf "${VCF_FILE}" \
  --out "${PLINK_FILE}"
echo "Done"

