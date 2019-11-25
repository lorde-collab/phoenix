#!/bin/bash
# Performs QC

anyfail=no
while read sample build rootname
do
  dir=$(pwd)/workspace/intmd/$sample/finish
  if ! qcquiet.sh $(pwd)/workspace/files-12-finalQC/failed_qc/$rootname qc_final_bam.sh $dir/$rootname.bam $dir/$rootname.flagstat.txt $(pwd)/workspace/intmd/$sample/unrefined/$rootname.flagstat.txt
  then anyfail=yes
  fi
done < sample_build.txt
if [ "$anyfail" == "yes" ]
then 
  echo There were QC failures
  exit 1
fi
