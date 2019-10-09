#!/bin/bash
# Convert ubam to fastq

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace

# Make commands script:
for sample in SJALL050550_D1 
do
  # Write commands
  make_script_ubam_to_fastq.sh /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/ubam /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd/$sample/fastq
done > /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-00.sh
