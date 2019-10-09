#!/bin/bash
# Write merge-refinement cmds to cmds file

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  refdir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/refine/mapping-config/$build
  # Write commands
  make_script_merge_refinement_files.sh GRCh37-lite $refdir/refinement
done > /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-08.sh
