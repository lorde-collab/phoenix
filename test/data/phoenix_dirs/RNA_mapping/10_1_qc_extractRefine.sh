#!/bin/bash
# Performs QC

anyfail=no
while read sample build rootname
do
  refdir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/refine/mapping-config/$build
  if ! qcquiet.sh /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/files-10-extractRefine/failed_qc/$sample qc_merged_refinements.sh $refdir/refinement 1 10 11 12 13 14 15 16 17 18 19 2 3 4 5 6 7 8 9 MT X Y 
  then anyfail=yes
  fi
done < sample_build.txt
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
