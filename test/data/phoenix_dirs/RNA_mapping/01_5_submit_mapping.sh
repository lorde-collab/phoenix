#!/usr/bin/env bash

exit_trap() {
    for pid in $(pgrep -P $$); do
        kill -9 $pid
    done
}
trap exit_trap EXIT

Phoenix-sub -K -P compbiores -J RNA_mapping.mapping -M 2500 -o /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/files-01-mapping/logs/out.%J.%I.txt -e /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/files-01-mapping/logs/err.%J.%I.txt -app mapping-rna-align-rsnm -i /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-01-RefSeq.nm.sh &
PIDS+=($!)
Phoenix-sub -K -P compbiores -J RNA_mapping.mapping -M 5000 -o /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/files-01-mapping/logs/out.%J.%I.txt -e /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/files-01-mapping/logs/err.%J.%I.txt -app mapping-rna-align-rsae -i /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-01-RefSeq.alt_exon.sh &
PIDS+=($!)
Phoenix-sub -K -P compbiores -J RNA_mapping.mapping -M 2500 -o /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/files-01-mapping/logs/out.%J.%I.txt -e /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/files-01-mapping/logs/err.%J.%I.txt -app mapping-rna-align-avnm -i /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-01-AceView.nm.sh &
PIDS+=($!)
Phoenix-sub -K -P compbiores -J RNA_mapping.mapping -M 5000 -o /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/files-01-mapping/logs/out.%J.%I.txt -e /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/files-01-mapping/logs/err.%J.%I.txt -app mapping-rna-align-wg -i /research/rgs01/scratch/tartan_prod/tIUDDrvkJu/workspace/cmds-01-WG.sh &
PIDS+=($!)

for pid in ${PIDS[@]}; do
    wait $pid
    STATUSES+=($?)
done

for STATUS in ${STATUSES[@]}; do
    if [[ $STATUS != 0 ]]; then
        exit $STATUS
    fi
done

