#!/bin/bash
# Write split-fasta cmds to cmds file

# Run from run dir for simplicity
cd $(pwd)/workspace

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  # Write commands
  make_script_split_big_fasta.sh $(pwd)/workspace/intmd/$sample/refine/mapping-config/$build/fasta $(pwd)/workspace/intmd/$sample/refine/mapping-config/$build/fasta-sized
done > $(pwd)/workspace/cmds-06.sh 
