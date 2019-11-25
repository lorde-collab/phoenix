#!/usr/bin/env bash

exit_trap() {
    for pid in $(pgrep -P $$); do
        kill -9 $pid
    done
}
trap exit_trap EXIT

Phoenix-sub -K -P compbiores -J yp1tkNml-post.mapping -M 2500 -o $(pwd)/workspace/files-01-mapping/logs/out.%J.%I.txt -e $(pwd)/workspace/files-01-mapping/logs/err.%J.%I.txt -app mapping-rna-align-rsnm -i $(pwd)/workspace/cmds-01-RefSeq.nm.sh &
PIDS+=($!)
Phoenix-sub -K -P compbiores -J yp1tkNml-post.mapping -M 5000 -o $(pwd)/workspace/files-01-mapping/logs/out.%J.%I.txt -e $(pwd)/workspace/files-01-mapping/logs/err.%J.%I.txt -app mapping-rna-align-rsae -i $(pwd)/workspace/cmds-01-RefSeq.alt_exon.sh &
PIDS+=($!)
Phoenix-sub -K -P compbiores -J yp1tkNml-post.mapping -M 2500 -o $(pwd)/workspace/files-01-mapping/logs/out.%J.%I.txt -e $(pwd)/workspace/files-01-mapping/logs/err.%J.%I.txt -app mapping-rna-align-avnm -i $(pwd)/workspace/cmds-01-AceView.nm.sh &
PIDS+=($!)
Phoenix-sub -K -P compbiores -J yp1tkNml-post.mapping -M 5000 -o $(pwd)/workspace/files-01-mapping/logs/out.%J.%I.txt -e $(pwd)/workspace/files-01-mapping/logs/err.%J.%I.txt -app mapping-rna-align-wg -i $(pwd)/workspace/cmds-01-WG.sh &
PIDS+=($!)
Phoenix-sub -K -P compbiores -J yp1tkNml-post.mapping -M 30000 -o $(pwd)/workspace/files-01-mapping/logs/out.%J.%I.txt -e $(pwd)/workspace/files-01-mapping/logs/err.%J.%I.txt -app mapping-rna-align-star -i $(pwd)/workspace/cmds-01-STAR.sh &
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

