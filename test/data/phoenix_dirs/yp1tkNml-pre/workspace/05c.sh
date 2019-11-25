#!/bin/bash
# Performs QC

anyfail=no
while read sample build rootname
do
  dir=$(pwd)/workspace/intmd/$sample/refine/mapping-config/$build/ExtractUnmapped
  if ! qcquiet.sh $(pwd)/workspace/files-05-FASTA/failed_qc/$sample qc_extract_unmapped.sh $dir 1 10 11 12 13 14 15 16 17 18 19 2 20 21 22 3 4 5 6 7 8 9 MT X Y 
  then anyfail=yes
  fi
done < sample_build.txt
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
