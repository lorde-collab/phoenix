#!/bin/bash
# Performs QC
anyfail=no
for sample in SJALL050550_D1 
do
  for subdir in AceView.nm RefSeq.nm RefSeq.alt_exon STAR WG
  do
    dir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/align/GRCh37-lite/$subdir
    bn=`basename $dir`
    if ! qcquiet.sh /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/files-02-resolve_merge/failed_qc/$bn-$sample qc_bam_dir.sh $dir /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/ubam queryname
    then anyfail=yes
    fi
  done
done
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
