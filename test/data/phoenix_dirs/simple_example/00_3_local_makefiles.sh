#!/usr/bin/env bash

N=$(shuf -i 10-20 -n 1)

for i in $(seq 0 $N); do
    M=$(shuf -i 10-20 -n 1)
    echo $M > ${i}.tmp
done
