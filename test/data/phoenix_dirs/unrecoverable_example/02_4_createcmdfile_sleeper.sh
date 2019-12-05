#!/usr/bin/env bash

for tmpfile in *.tmp; do
    if [[ ! -f $tmpfile ]]; then
        continue
    fi
    nsecs=$(cat $tmpfile)
    echo "date && echo 'Sleeping for $nsecs' && sleep $nsecs && echo 'Wake up!' && date && exit $nsecs"
done > cmds-02.sh
