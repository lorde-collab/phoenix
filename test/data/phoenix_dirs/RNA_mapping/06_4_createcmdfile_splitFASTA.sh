#!/bin/bash
# Write split-fasta cmds to cmds file

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  # Write commands
  make_script_split_big_fasta.sh /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/nRZ0IX0M/intmd/$sample/refine/mapping-config/$build/fasta /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/nRZ0IX0M/intmd/$sample/refine/mapping-config/$build/fasta-sized
done > /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/cmds-06.sh 
