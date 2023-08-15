#!/bin/bash

features=(
  "gene"
  "transcript"
  "exon"
  "CDS"
)

for feature in "${features[@]}"
do
  bedtools multicov -bams /tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/sorted_final_bam_v2/*_sorted.bam \
    -bed "../data/106_annotation_ema/features/${feature}.bed" \
    > "../data/106_annotation_ema/coverage/${feature}.txt"
done