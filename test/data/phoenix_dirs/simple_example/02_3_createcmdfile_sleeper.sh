#!/usr/bin/env bash

for tmpfile in *.tmp; do
    nsecs=$(cat $tmpfile)
    echo "date && echo 'Sleeping for $nsecs' && sleep $nsecs && echo 'Wake up!' && date"
done > cmds-02.sh
