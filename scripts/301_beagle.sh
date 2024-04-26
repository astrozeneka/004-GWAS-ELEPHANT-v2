#!/bin/bash
#SBATCH -p memory
#SBATCH -N 1 -c 96
#SBATCH -t 24:00:00
#SBATCH --mem=100GB
#SBATCH -J beagle
#SBATCH -A proj5034

mkdir -p ../data/2001_beagle
VCF_FILE="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/plink_ema_hair_chr123/populations.snps.vcf"


# Reorder the vcf file using BCFtools sort
module load BCFtools
bcftools sort -o ../data/2001_beagle/populations.snps.sorted.vcf ${VCF_FILE}

# Remove duplicates using bcftools norm
bcftools norm -D -o ../data/2001_beagle/populations.snps.sorted.norm.vcf ../data/2001_beagle/populations.snps.sorted.vcf

# Use beagle software to impute missing genotypes
java -jar /tarafs/data/home/hrasoara/softwares/beagle.22Jul22.46e.jar \
	gt=../data/2001_beagle/populations.snps.sorted.norm.vcf \
	out=../data/2001_beagle/populations.snps.imputed.vcf

echo "Imputation done"