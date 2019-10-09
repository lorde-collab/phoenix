#!/bin/bash
# Write merge-markdup-index cmds to cmds file

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace

# Make commands script:
make_script_mmi_from_run_config.sh /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/mapping-config /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/intmd align/GRCh37-lite/resolve-merged unrefined > /research/rgs01/scratch/tartan_prod/t_7OHnDQHK/workspace/cmds-03.sh 
