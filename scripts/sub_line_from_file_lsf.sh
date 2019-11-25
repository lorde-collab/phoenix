#!/usr/bin/env bash
# Given the '$LSB_JOBINDEX' environment variable and an input file, this
# this script will evaluate the '$LSB_JOBINDEX'th line of the file.

if [[ ! -f $1 ]]; then
    >&2 echo "ERROR: No commandfile given"
    >&2 echo "Usage: sub_line_from_file_lsf.sh /path/to/cmdfile.txt"
    exit 1
fi

eval $(head -n $LSB_JOBINDEX $1 | tail -n 1)
