#!/usr/bin/env bash
parallel ::: \
"Phoenix-sub -K -P compbiores -J workspace-1.merge -M 3808 -oo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-08-merge/logs/out.%J.%I.txt -eo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-08-merge/logs/err.%J.%I.txt -app mapping-rna-refmrg -i /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/cmds-08.sh" 