#!/bin/bash
# Write merge-markdup-index cmds to cmds file

# Run from run dir for simplicity
cd $(pwd)/workspace

# Make commands script:
make_script_mmi_from_run_config.sh /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/yp1tkNml/mapping-config $(pwd)/workspace/intmd align/GRCh37-lite/resolve-merged unrefined > $(pwd)/workspace/cmds-03.sh 
