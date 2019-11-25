#!/bin/bash
# Performs QC

anyfail=no
while read sample build rootname
do
  dir=$(pwd)/workspace/intmd/$sample/refine/mapping-config/$build/fasta
  if ! qcquiet.sh $(pwd)/workspace/files-06-splitFASTA/failed_qc/$sample qc_refine_fasta.sh $dir /research/rgs01/resgen/prod/tartan/runs/ad_hoc/reference_import-Tm4OgjZi/output/reference/Homo_sapiens/GRCh37-lite/SUPPORT/windows.txt 20 31
  then anyfail=yes
  fi
done < sample_build.txt
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
