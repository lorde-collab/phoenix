#!/bin/bash
# Performs QC

anyfail=no
for sample in SJALL050550_D1 
do
  dir=$(pwd)/workspace/intmd/$sample/align/GRCh37-lite/resolve-merged
  if ! qcquiet.sh $(pwd)/workspace/files-03-finishalign/failed_qc/$sample qc_bam_dir.sh $dir $(pwd)/workspace/intmd/$sample/ubam coordinate
  then anyfail=yes
  fi
done
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
