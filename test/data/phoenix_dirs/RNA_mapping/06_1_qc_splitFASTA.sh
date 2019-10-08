#!/bin/bash
# Performs QC

anyfail=no
while read sample build rootname
do
  dir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/nRZ0IX0M/intmd/$sample/refine/mapping-config/$build/fasta
  if ! qcquiet.sh /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-06-splitFASTA/failed_qc/$sample qc_refine_fasta.sh $dir /research/rgs01/resgen/prod/tartan/runs/ad_hoc/reference_import-Tm4OgjZi/output/reference/Homo_sapiens/GRCh37-lite/SUPPORT/windows.txt 20 31
  then anyfail=yes
  fi
done < sample_build.txt
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
