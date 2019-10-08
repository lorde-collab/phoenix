#!/bin/bash
# Performs QC
anyfail=no
for sample in SJALL003423_D1 SJALL041091_D1 SJALL041092_D1 SJALL041093_D1 SJALL041095_D1 SJALL041097_D1 SJALL041106_D1 SJALL041107_D1 SJALL041108_D1 SJALL041109_D1 SJALL041111_D1 SJALL041113_D1 SJALL048273_D1 SJALL048277_D1 SJALL048278_D1 SJALL048280_D1 SJALL048291_D1 SJALL048292_D1 SJALL048293_D1 SJALL048294_D1 SJAML016326_D1 SJAML016327_D1 SJAML016328_D1 SJAML016329_D1 SJAML016330_D1 SJAML041098_D1 SJAML041099_D1 SJAML048272_D1 SJAML048274_D1 SJAML048279_D1 SJAML048282_D1 SJAML054711_D1 SJAML054728_D1 SJAML054729_D1 SJAML054730_D1 SJAML054733_D1 SJINF015832_D1 SJINF015833_D1 SJINF015834_D1 SJINF026_D SJINF027_D SJINF041089_D1 SJINF041100_D1 SJINF041101_D1 SJINF041102_D1 SJINF041103_D1 SJINF041104_D1 SJINF045380_D1 SJINF045380_R2 SJINF048147_D1 SJINF048148_D1 SJINF048149_D1 SJINF048275_D1 SJINF048276_D1 SJINF048281_D1 SJINF048283_D1 SJINF048284_D1 SJINF048285_D1 SJINF048290_D1 SJINF054707_D1 SJINF054726_D1 SJINF054727_D1 SJINF054732_D1 
do
  for subdir in AceView.nm RefSeq.nm RefSeq.alt_exon STAR WG
  do
    dir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/nRZ0IX0M/intmd/$sample/align/GRCh37-lite/$subdir
    bn=`basename $dir`
    if ! qcquiet.sh /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-02-resolve_merge/failed_qc/$bn-$sample qc_bam_dir.sh $dir /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/nRZ0IX0M/intmd/$sample/ubam queryname
    then anyfail=yes
    fi
  done
done
if [ "$anyfail" == "yes" ]
then
  echo There were QC failures
  exit 1
fi
