#!/bin/bash

for fp in `ls -d gene-fastas/*`
do
    fn=`basename $fp`
    nseqs=`grep -P '\>' $fp | wc -l`
    if [ $nseqs -gt 1 ]
    then
        echo $fp
        ./clustalo -i $fp --full --force --distmat-out=idmats/$fn.pid --percent-id > /dev/null
    fi
done