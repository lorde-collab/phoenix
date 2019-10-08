#!/usr/bin/env bash
parallel ::: \
"Phoenix-sub -K -P compbiores -J workspace-1.finishalign -M 15000 -oo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-03-finishalign/logs/out.%J.%I.txt -eo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-03-finishalign/logs/err.%J.%I.txt -app mapping-rna-finish1 -i /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/cmds-03.sh" 