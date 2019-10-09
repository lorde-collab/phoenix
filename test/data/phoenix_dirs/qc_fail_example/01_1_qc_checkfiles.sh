#!/usr/bin/env bash

ls *.tmp 1> /dev/null 2> /dev/null
exit_code=$?

if [[ $exit_code != 0 ]]; then
    exit $exit_code
fi
