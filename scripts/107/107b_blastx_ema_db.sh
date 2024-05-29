#!/bin/bash
#SBATCH -p memory
#SBATCH -N 1 -c 120
#SBATCH -t 5-00:00:00
#SBATCH -J BWAjob
#SBATCH -A proj5034

module load BLAST+/2.12.0-gompi-2021a
# module load BLAST+/2.10.0-gompi-2019b
source ~/.bashrc

FASTA_CUT_DIRECTORY="/tarafs/data/home/hrasoara/Projects/004-GWAS-ELEPHANT-v2/data/104_fasta_cutted"
OUTPUT_DIRECTORY="/tarafs/data/home/hrasoara/Projects/004-GWAS-ELEPHANT-v2/data/107_blast_output"
export BLASTDB="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/EMA_genome/ncbi-ema_database"
slugs=(
  "hair-pot"
  "hair-sig"
  "tusk-pot"
  "tusk-sig"
)
for slug in "${slugs[@]}"
do
  blastx -query "${FASTA_CUT_DIRECTORY}/${slug}.fasta" \
    -db protein.faa \
    -num_threads 120 \
    -out "${OUTPUT_DIRECTORY}/${slug}.xml" \
    -evalue 0.001 \
    -outfmt 5
done
echo "Done"
