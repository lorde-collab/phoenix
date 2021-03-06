#!/bin/bash
# Write extract-unmapped cmds to cmds file

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  # Write commands
  make_script_extract_unmapped_chr.sh MGSCv37 /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/unrefined/$rootname.bam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/refine/mapping-config/$build/ExtractUnmapped
done > /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-04.sh
