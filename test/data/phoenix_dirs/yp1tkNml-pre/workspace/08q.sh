#!/bin/bash
# Write merge-refinement cmds to cmds file

# Run from run dir for simplicity
cd $(pwd)/workspace

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  refdir=$(pwd)/workspace/intmd/$sample/refine/mapping-config/$build
  # Write commands
  make_script_merge_refinement_files.sh GRCh37-lite $refdir/refinement
done > $(pwd)/workspace/cmds-08.sh
