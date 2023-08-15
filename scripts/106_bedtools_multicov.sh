#!/bin/bash

features=(
  "gene"
  "transcript"
  "exon"
  "CDS"
)

for feature in "${features[@]}"
do
  bedtools multicov --bams /tarafs/data/home/hrasoara/proj5034-AGBKU/map_bwa_ema_Ryan/final_bam/*.bam \
    -bed "../data/106_annotation_ema/features/${feature}.bed" \
    > "../data/106_annotation_ema/covearge/${feature}.txt"
done