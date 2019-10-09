#!/bin/bash
# Writes resolve-merge commands to cmds file

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace

# Make commands script:
for sample in SJMMINF063855_D1 SJMMINF063856_D1 SJMMINF063857_D1 SJMMINF063858_D1 SJMMINF063859_D1 
do
  # Get ordered dir list
  dirs=
  for subdir in AceView.nm RefSeq.nm RefSeq.alt_exon WG
  do
    dir="/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/align/MGSCv37/$subdir"
    if [ -d "$dir" ]; then dirs="$dirs $dir"; fi
  done
  # Write commands
  make_script_resmrg_rgmerge.sh MGSCv37 /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/ubam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/align/MGSCv37/resolve-merged $dirs
done > /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-02.sh 
