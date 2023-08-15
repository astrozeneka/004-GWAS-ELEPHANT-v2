#!/bin/bash
#SBATCH -p memory
#SBATCH -N 1 -c 96
#SBATCH -t 5-00:00:00
#SBATCH -J BWAjob
#SBATCH -A proj5034

module purge
module load SAMtools/1.9-intel-2019b

MAP_DIRECTORY="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/final_bam"
OUTPUT_DIRECTORY="/tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/sorted_final_bam_v2"

genomes=(
    "EMAf10_q20"
    "EMAf1_q20"
    "EMAf28_q20"
    "EMAf2_q20"
    "EMAf3_q20"
    "EMAf4_q20"
    "EMAf5_q20"
    "EMAf7_q20"
    "EMAFf20_q20"
    "EMAFf21_q20"
    "EMAFf2_q20"
    "EMAFf5_q20"
    "EMAFf6_q20"
    "EMAFm2_q20"
    "EMAFm6_q20"
    "EMAFm9_q20"
    "EMAm10_q20"
    "EMAm12_q20"
    "EMAm13_q20"
    "EMAm14_q20"
    "EMAm16_q20"
    "EMAm17_q20"
    "EMAm18_q20"
    "EMAm19_q20"
    "EMAm1_q20"
    "EMAm20_q20"
    "EMAm2_q20"
    "EMAm3_q20"
    "EMAm5_q20"
    "EMAm6_q20"
    "EMAm7_q20"
    "EMAm8_q20"
    "EMAm9_q20"
)
genomes=(
  "EMAf10_q20"
)
for genome in "${genomes[@]}"
do
  echo " "
  echo samtools sort "${MAP_DIRECTORY}/${genome}.bam" \
    -o "${OUTPUT_DIRECTORY}/${genome}_sorted.sorted"
  echo samtools index -@ 96 "${OUTPUT_DIRECTORY}/${genome}_sorted.sorted"
done