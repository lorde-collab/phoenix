#!/bin/bash
# Write extract-unmapped cmds to cmds file

# Run from run dir for simplicity
cd $(pwd)/workspace

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  # Write commands
  make_script_extract_unmapped_chr.sh GRCh37-lite $(pwd)/workspace/intmd/$sample/unrefined/$rootname.bam $(pwd)/workspace/intmd/$sample/refine/mapping-config/$build/ExtractUnmapped
done > $(pwd)/workspace/cmds-04.sh
