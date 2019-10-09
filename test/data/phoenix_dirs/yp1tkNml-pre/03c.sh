#!/bin/bash
# Performs QC

anyfail=no
for sample in SJALL050550_D1 
do
  dir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/align/GRCh37-lite/resolve-merged
  if ! qcquiet.sh /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/files-03-finishalign/failed_qc/$sample qc_bam_dir.sh $dir /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/ubam coordinate
  then anyfail=yes
  fi
done
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
