#!/usr/bin/env bash
parallel ::: \
"Phoenix-sub -K -P compbiores -J workspace-1.globalNames -M 3808 -oo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-09-globalNames/logs/out.%J.%I.txt -eo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-09-globalNames/logs/err.%J.%I.txt -app mapping-rna-names -i /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/cmds-09.sh" 