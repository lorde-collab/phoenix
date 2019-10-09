#!/bin/bash
# Compile mapping stats

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace

# Stats
echo Mapping stats are written to mapping_stats.txt and are presented here:
( cd /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd; compile_mapping_stats.sh -h SJALL050550_D1  ) | tee mapping_stats.txt
awk '{ ndm=$4; gsub(/,/, "", ndm); print $1, ndm }' mapping_stats.txt | sample_qc.sh "Mapping Stats" NonDupMapped 0
