#!/bin/bash
# Performs QC

anyfail=no
while read sample build rootname
do
  refdir=$(pwd)/workspace/intmd/$sample/refine/mapping-config/$build
  if ! qcquiet.sh $(pwd)/workspace/files-08-merge/failed_qc/$sample qc_sim4_refinements.sh $refdir/refinement $refdir/fasta-sized
  then anyfail=yes
  fi
done < sample_build.txt
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
