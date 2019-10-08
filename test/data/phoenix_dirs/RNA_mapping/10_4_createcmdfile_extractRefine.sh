#!/bin/bash
# Write extract-refine cmds to cmds file

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  refdir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/nRZ0IX0M/intmd/$sample/refine/mapping-config/$build
  # Write commands
  make_script_extract_refine.sh GRCh37-lite /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/nRZ0IX0M/intmd/$sample/unrefined/$rootname.bam $refdir/refinement $refdir/bam -A
done > /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/cmds-10.sh
