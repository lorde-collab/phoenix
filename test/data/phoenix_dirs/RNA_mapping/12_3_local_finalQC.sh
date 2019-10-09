#!/bin/bash
# Compile mapping stats

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace

# Stats
echo Mapping stats are written to mapping_stats.txt and are presented here:
( cd /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd; compile_mapping_stats.sh -h SJMMINF063855_D1 SJMMINF063856_D1 SJMMINF063857_D1 SJMMINF063858_D1 SJMMINF063859_D1  ) | tee mapping_stats.txt
awk '{ ndm=$4; gsub(/,/, "", ndm); print $1, ndm }' mapping_stats.txt | sample_qc.sh "Mapping Stats" NonDupMapped 0
