#!/usr/bin/env bash
parallel ::: \
"Phoenix-sub -K -P compbiores -J workspace-1.finish -M 16000 -oo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-11-finish/logs/out.%J.%I.txt -eo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-11-finish/logs/err.%J.%I.txt -app mapping-rna-finish2 -i /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/cmds-11.sh" 