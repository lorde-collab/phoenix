#!/bin/bash
# Performs QC

anyfail=no
while read sample build rootname
do
  refdir=$(pwd)/workspace/intmd/$sample/refine/mapping-config/$build
  if ! qcquiet.sh $(pwd)/workspace/files-11-finish/failed_qc/$sample qc_extrref_bams.sh $refdir/bam $(pwd)/workspace/intmd/$sample/unrefined/$rootname.bam $refdir/refinement
  then anyfail=yes
  fi
done < sample_build.txt
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
