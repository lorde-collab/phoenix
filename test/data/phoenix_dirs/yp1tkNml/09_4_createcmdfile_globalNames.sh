#!/bin/bash
# Write create-refined-names cmds to cmds file

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace

# No QC
echo FYI No QC for refinement merging.  QC is after next step

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  refdir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/refine/mapping-config/$build
  echo create_refined_names_file.sh $refdir/refinement/names.txt $refdir/refinement/merged-*.txt
done > /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-09.sh 
