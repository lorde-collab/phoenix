#!/usr/bin/env bash
parallel ::: \
"Phoenix-sub -K -P compbiores -J workspace-1.splitFASTA -M 3808 -oo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-06-splitFASTA/logs/out.%J.%I.txt -eo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-06-splitFASTA/logs/err.%J.%I.txt -app mapping-rna-splitfasta -i /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/cmds-06.sh" 