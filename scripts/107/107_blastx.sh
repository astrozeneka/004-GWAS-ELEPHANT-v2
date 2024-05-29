#!/bin/bash
#SBATCH -p memory
#SBATCH -N 1 -c 96
#SBATCH -t 5-00:00:00
#SBATCH -J BWAjob
#SBATCH -A proj5034

FASTA_CUT_DIRECTORY="/tarafs/data/home/hrasoara/Projects/004-GWAS-ELEPHANT-v2/data/104_fasta_cutted"
DATABASE="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/protein_db/nr"
OUTPUT_DIRECTORY="/tarafs/data/home/hrasoara/Projects/004-GWAS-ELEPHANT-v2/data/107_blast_output"
slug=(
  "hair-pot"
  "hair-sig"
  "tusk-pot"
  "tusk-sig"
)
for slug in "${slugs[@]}"
do
  echo blastx -query "${FASTA_CUT_DIRECTORY}/${slug}.fasta" \
    -db "${DATABASE}" \
    -out "${OUTPUT_DIRECTORY}" \
    -evalue 0.001 \
    -outfmt 6
  exit
done
