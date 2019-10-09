#!/bin/bash
# Write fixmateinfo cmds to cmds file

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  refdir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/refine/mapping-config/$build
  # Write commands
  echo fixmateinfo_merge_markdup_index.sh /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/finish/$rootname.bam $refdir/bam/refined*.bam -- $refdir/bam/unrefined*.bam
done > /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-11.sh
