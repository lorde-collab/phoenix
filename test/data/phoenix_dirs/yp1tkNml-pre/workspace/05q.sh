#!/bin/bash
# Write extract-windowed-fasta cmds to cmds file

# Run from run dir for simplicity
cd $(pwd)/workspace

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  # Write commands
  make_script_extract_windowed_fasta.sh GRCh37-lite $(pwd)/workspace/intmd/$sample/refine/mapping-config/$build/ExtractUnmapped $(pwd)/workspace/intmd/$sample/refine/mapping-config/$build/fasta 4
done > $(pwd)/workspace/cmds-05.sh 
