#!/bin/bash
# Write extract-refine cmds to cmds file

# Run from run dir for simplicity
cd $(pwd)/workspace

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  refdir=$(pwd)/workspace/intmd/$sample/refine/mapping-config/$build
  # Write commands
  make_script_extract_refine.sh GRCh37-lite $(pwd)/workspace/intmd/$sample/unrefined/$rootname.bam $refdir/refinement $refdir/bam -A
done > $(pwd)/workspace/cmds-10.sh
