#!/bin/bash
# Performs QC

anyfail=no
while read sample build rootname
do
  refdir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/nRZ0IX0M/intmd/$sample/refine/mapping-config/$build
  if ! qcquiet.sh /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-11-finish/failed_qc/$sample qc_extrref_bams.sh $refdir/bam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/nRZ0IX0M/intmd/$sample/unrefined/$rootname.bam $refdir/refinement
  then anyfail=yes
  fi
done < sample_build.txt
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
