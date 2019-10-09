#!/bin/bash
# Performs QC
anyfail=no
for sample in SJMMINF063855_D1 SJMMINF063856_D1 SJMMINF063857_D1 SJMMINF063858_D1 SJMMINF063859_D1 
do
  for subdir in AceView.nm RefSeq.nm RefSeq.alt_exon WG
  do
    dir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/align/MGSCv37/$subdir
    bn=`basename $dir`
    if ! qcquiet.sh /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/files-02-resolve_merge/failed_qc/$bn-$sample qc_bam_dir.sh $dir /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/ubam queryname
    then anyfail=yes
    fi
  done
done
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
