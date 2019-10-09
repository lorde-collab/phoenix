#!/bin/bash
# Performs QC

anyfail=no
for sample in SJMMINF063855_D1 SJMMINF063856_D1 SJMMINF063857_D1 SJMMINF063858_D1 SJMMINF063859_D1 
do
  dir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/align/MGSCv37/resolve-merged
  if ! qcquiet.sh /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/files-03-finishalign/failed_qc/$sample qc_bam_dir.sh $dir /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/ubam coordinate
  then anyfail=yes
  fi
done
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
