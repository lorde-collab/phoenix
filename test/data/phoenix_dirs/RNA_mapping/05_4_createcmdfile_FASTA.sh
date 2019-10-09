#!/bin/bash
# Write extract-windowed-fasta cmds to cmds file

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  # Write commands
  make_script_extract_windowed_fasta.sh MGSCv37 /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/refine/mapping-config/$build/ExtractUnmapped /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/refine/mapping-config/$build/fasta 4
done > /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-05.sh 
