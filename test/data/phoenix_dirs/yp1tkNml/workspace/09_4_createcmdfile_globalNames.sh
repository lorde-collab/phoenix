#!/bin/bash
# Write create-refined-names cmds to cmds file

# Run from run dir for simplicity
cd $(pwd)/workspace

# No QC
echo FYI No QC for refinement merging.  QC is after next step

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  refdir=$(pwd)/workspace/intmd/$sample/refine/mapping-config/$build
  echo create_refined_names_file.sh $refdir/refinement/names.txt $refdir/refinement/merged-*.txt
done > $(pwd)/workspace/cmds-09.sh 
