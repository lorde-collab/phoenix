#!/bin/bash
# Performs QC

anyfail=no
while read sample build rootname
do
  dir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/refine/mapping-config/$build/fasta
  if ! qcquiet.sh /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/files-06-splitFASTA/failed_qc/$sample qc_refine_fasta.sh $dir /research/rgs01/resgen/prod/tartan/runs/tartan_import/0uJkminb/output/SUPPORT/windows.txt 4 10
  then anyfail=yes
  fi
done < sample_build.txt
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
