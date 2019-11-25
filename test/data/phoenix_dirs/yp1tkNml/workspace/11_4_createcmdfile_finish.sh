#!/bin/bash
# Write fixmateinfo cmds to cmds file

# Run from run dir for simplicity
cd $(pwd)/workspace

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  refdir=$(pwd)/workspace/intmd/$sample/refine/mapping-config/$build
  # Write commands
  echo fixmateinfo_merge_markdup_index.sh $(pwd)/workspace/intmd/$sample/finish/$rootname.bam $refdir/bam/refined*.bam -- $refdir/bam/unrefined*.bam
done > $(pwd)/workspace/cmds-11.sh
