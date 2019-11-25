#!/bin/bash
# Compile mapping stats

# Run from run dir for simplicity
cd $(pwd)/workspace

# Stats
echo Mapping stats are written to mapping_stats.txt and are presented here:
( cd $(pwd)/workspace/intmd; compile_mapping_stats.sh -h SJALL050550_D1  ) | tee mapping_stats.txt
awk '{ ndm=$4; gsub(/,/, "", ndm); print $1, ndm }' mapping_stats.txt | sample_qc.sh "Mapping Stats" NonDupMapped 0
