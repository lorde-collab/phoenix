#!/bin/bash
# Write batch-sim4 commands

# Run from run dir for simplicity
cd $(pwd)/workspace

# No QC
echo FYI No QC for fasta splitting.  QC is after next step

# Make commands script:
cat sample_build.txt | while read sample build rootname
do
  refdir=$(pwd)/workspace/intmd/$sample/refine/mapping-config/$build
  batch_sim4_and_make_script.sh GRCh37-lite $refdir/fasta-sized $refdir/refinement $refdir/sim4_batches
done > $(pwd)/workspace/cmds-07.sh 
