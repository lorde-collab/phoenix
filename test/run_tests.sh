#!/usr/bin/env bash

cd $(dirname ${0})

module load python/3.5.2

export PYTHONPATH=$(pwd)/../src:$PYTHONPATH
export PATH=$(pwd)/../scripts:$PATH

#phoenix run -d data/phoenix_dirs/simple_example

#exit 0

coverage run -m --source ../src/phoenix unittest discover unit_tests -p "*test.py" -b
coverage_report=$(mktemp)
coverage report -m > $coverage_report
cat $coverage_report
rm $coverage_report

