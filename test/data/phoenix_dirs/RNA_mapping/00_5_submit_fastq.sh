#!/usr/bin/env bash
parallel ::: \
"Phoenix-sub -K -P compbiores -J workspace-1.fastq -M 3808 -oo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-00-fastq/logs/out.%J.%I.txt -eo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-00-fastq/logs/err.%J.%I.txt -app mapping-rna-fasta -i /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/cmds-00.sh" 