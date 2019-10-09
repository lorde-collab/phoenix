#!/bin/bash
# Write merge-markdup-index cmds to cmds file

# Run from run dir for simplicity
cd /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace

# Make commands script:
make_script_mmi_from_run_config.sh /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/mapping-config /research/rgs01/resgen/prod/tartan/runs/RNA_mapping/ZzV6R6wi/intmd align/MGSCv37/resolve-merged unrefined > /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-03.sh 
