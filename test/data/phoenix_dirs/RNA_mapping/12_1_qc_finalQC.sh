#!/bin/bash
# Performs QC

anyfail=no
while read sample build rootname
do
  dir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/nRZ0IX0M/intmd/$sample/finish
  if ! qcquiet.sh /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-12-finalQC/failed_qc/$rootname qc_final_bam.sh $dir/$rootname.bam $dir/$rootname.flagstat.txt /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/nRZ0IX0M/intmd/$sample/unrefined/$rootname.flagstat.txt
  then anyfail=yes
  fi
done < sample_build.txt
if [ "$anyfail" == "yes" ]
then 
  echo There were QC failures
  exit 1
fi
