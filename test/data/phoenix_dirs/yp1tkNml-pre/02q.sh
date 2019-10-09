#!/bin/bash
# Writes resolve-merge commands to cmds file

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace

# Make commands script:
for sample in SJALL050550_D1 
do
  # Get ordered dir list
  dirs=
  for subdir in AceView.nm RefSeq.nm RefSeq.alt_exon STAR WG
  do
    dir="/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/align/GRCh37-lite/$subdir"
    if [ -d "$dir" ]; then dirs="$dirs $dir"; fi
  done
  # Write commands
  make_script_resmrg_rgmerge.sh GRCh37-lite /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/ubam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/align/GRCh37-lite/resolve-merged $dirs
done > /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-02.sh 
