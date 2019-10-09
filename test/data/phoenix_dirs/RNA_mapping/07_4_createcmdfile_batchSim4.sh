#!/bin/bash
# Write batch-sim4 commands

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace

# No QC
echo FYI No QC for fasta splitting.  QC is after next step

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  refdir=/research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd/$sample/refine/mapping-config/$build
  batch_sim4_and_make_script.sh MGSCv37 $refdir/fasta-sized $refdir/refinement $refdir/sim4_batches
done > /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-07.sh 
