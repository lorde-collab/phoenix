#!/bin/bash
# Do mapping

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace

# Write commands file for RefSeq.nm
for sample in SJALL050550_D1 
do
  make_script_bwa_alignxe_ubam_qn_xlate.sh GRCh37-lite /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/ubam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/align/GRCh37-lite/RefSeq.nm precopy REFSEQ_NM -s 3 -p 2
done > /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-01-RefSeq.nm.sh

# Write commands file for RefSeq.alt_exon
for sample in SJALL050550_D1 
do
  make_script_bwa_alignxe_ubam_qn_xlate.sh GRCh37-lite /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/ubam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/align/GRCh37-lite/RefSeq.alt_exon precopy REFSEQ_AE -s 3 -p 3
done > /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-01-RefSeq.alt_exon.sh

# Write commands file for AceView.nm
for sample in SJALL050550_D1 
do
  make_script_bwa_alignxe_ubam_qn_xlate.sh GRCh37-lite /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/ubam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/align/GRCh37-lite/AceView.nm precopy ACEVIEW_NM -s 3 -p 4
done > /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-01-AceView.nm.sh

# Write commands file for WG
for sample in SJALL050550_D1 
do
  make_script_bwa_alignxe_ubam_qn.sh GRCh37-lite /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/ubam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/align/GRCh37-lite/WG precopy WG -s 3 -p 5
done > /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-01-WG.sh

# Write commands file for STAR
for sample in SJALL050550_D1 
do
  make_script_star_alignxe_fq_qn.sh GRCh37-lite /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/fastq /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/align/GRCh37-lite/STAR precopy WG -s 3 -p 6
done > /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-01-STAR.sh

