#!/usr/bin/env bash

cd $(dirname ${0})

module load python/3.5.2

export PYTHONPATH=$(pwd)/../src:$PYTHONPATH
export PATH=$(pwd)/../scripts:$PATH

phoenix run -d data/phoenix_dirs/RNA_mapping

