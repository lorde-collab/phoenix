#!/bin/bash
# Performs QC
anyfail=no
for sample in SJALL050550_D1 
do
  for subdir in AceView.nm RefSeq.nm RefSeq.alt_exon STAR WG
  do
    dir=$(pwd)/workspace/intmd/$sample/align/GRCh37-lite/$subdir
    bn=`basename $dir`
    if ! qcquiet.sh $(pwd)/workspace/files-02-resolve_merge/failed_qc/$bn-$sample qc_bam_dir.sh $dir $(pwd)/workspace/intmd/$sample/ubam queryname
    then anyfail=yes
    fi
  done
done
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
