#!/bin/bash
# Create a blast database from a protein Sequence

module load BLAST+/2.12.0-gompi-2021a

DB_DIRECTORY="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/EMA_genome/ncbi-ema_database"
DB_FILE="protein.faa"

makeblastdb -in "${DB_DIRECTORY}/${DB_FILE}" \
    -dbtype prot \
    -parse_seqids

echo "Done"
