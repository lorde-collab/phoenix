#!/bin/bash
# Do mapping

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace

# Write commands file for RefSeq.nm
for sample in SJMMINF063855_D1 SJMMINF063856_D1 SJMMINF063857_D1 SJMMINF063858_D1 SJMMINF063859_D1 
do
  make_script_bwa_alignxe_ubam_qn_xlate.sh MGSCv37 /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/ubam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/align/MGSCv37/RefSeq.nm precopy REFSEQ_NM -s 3 -p 2
done > /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-01-RefSeq.nm.sh

# Write commands file for RefSeq.alt_exon
for sample in SJMMINF063855_D1 SJMMINF063856_D1 SJMMINF063857_D1 SJMMINF063858_D1 SJMMINF063859_D1 
do
  make_script_bwa_alignxe_ubam_qn_xlate.sh MGSCv37 /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/ubam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/align/MGSCv37/RefSeq.alt_exon precopy REFSEQ_AE -s 3 -p 3
done > /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-01-RefSeq.alt_exon.sh

# Write commands file for AceView.nm
for sample in SJMMINF063855_D1 SJMMINF063856_D1 SJMMINF063857_D1 SJMMINF063858_D1 SJMMINF063859_D1 
do
  make_script_bwa_alignxe_ubam_qn_xlate.sh MGSCv37 /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/ubam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/align/MGSCv37/AceView.nm precopy ACEVIEW_NM -s 3 -p 4
done > /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-01-AceView.nm.sh

# Write commands file for WG
for sample in SJMMINF063855_D1 SJMMINF063856_D1 SJMMINF063857_D1 SJMMINF063858_D1 SJMMINF063859_D1 
do
  make_script_bwa_alignxe_ubam_qn.sh MGSCv37 /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/ubam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/align/MGSCv37/WG precopy WG -s 3 -p 5
done > /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-01-WG.sh

