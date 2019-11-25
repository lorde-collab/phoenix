#!/bin/bash
# Convert ubam to fastq

# Run from run dir for simplicity
cd $(pwd)/workspace

# Make commands script:
for sample in SJALL050550_D1 
do
  # Write commands
  make_script_ubam_to_fastq.sh $(pwd)/intmd/$sample/ubam $(pwd)/intmd/$sample/fastq
done > $(pwd)/workspace/cmds-00.sh
