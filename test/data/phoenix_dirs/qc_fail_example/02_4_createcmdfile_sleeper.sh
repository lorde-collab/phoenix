#!/usr/bin/env bash

for txtfile in *.txt; do
    nsecs=$(cat $txtfile)
    echo "date && echo 'Sleeping for $nsecs' && sleep $nsecs && echo 'Wake up!' && date"
done > cmds-02.sh
