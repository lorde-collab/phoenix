#!/bin/bash
# Convert ubam to fastq

# Run from run dir for simplicity
#cd /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace

# Make commands script:
for sample in SJMMINF063855_D1 SJMMINF063856_D1 SJMMINF063857_D1 SJMMINF063858_D1 SJMMINF063859_D1 
do
  # Write commands
  echo "echo /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/ubam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/fastq && sleep 4"
done > /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-00.sh
