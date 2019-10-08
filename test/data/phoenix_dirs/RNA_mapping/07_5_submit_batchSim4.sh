#!/usr/bin/env bash
parallel ::: \
"Phoenix-sub -K -P compbiores -J workspace-1.batchSim4 -M 3808 -oo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-07-batchSim4/logs/out.%J.%I.txt -eo /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/files-07-batchSim4/logs/err.%J.%I.txt -app mapping-rna-sim4 -i /research/rgs01/scratch/tartan_prod/RdUXkN3rhZ/workspace/cmds-07.sh" 