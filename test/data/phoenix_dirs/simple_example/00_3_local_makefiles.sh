#!/usr/bin/env bash

N=$(shuf -i 1-5 -n 1)
N=5

for i in $(seq 0 $N); do
    #M=$(shuf -i 10-20 -n 1)
    M=$i
    echo $M > ${i}.tmp
done
