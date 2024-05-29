#!/bin/bash
#SBATCH -p compute
#SBATCH -N 1 -c 1
#SBATCH -t 01:00:00
#SBATCH -J bedtools_getfasta
#SBATCH -A proj5034

module load BEDTools/2.28.0-intel-2019b

FASTA_DIRECTORY="/tarafs/data/home/hrasoara/gwas-ema"
FASTA_FILE="GCA_024166365.1_mEleMax1_primary_haplotype_genomic.fna"

slugs=(
	"hair-pot"
	"hair-sig"
	"tusk-pot"
	"tusk-sig"
)

for slug in "${slugs[@]}"
do
	bedtools getfasta -fi "${FASTA_DIRECTORY}/${FASTA_FILE}" \
		-bed ../data/103_bed_files/${slug}.bed \
		-fo ../data/104_fasta_cutted/${slug}.fasta 
	echo "${slug} done"
done
echo "all done"
