#!/bin/bash 
 clear

sh mtx2ispan.sh &> mtx2ispan.txt & 

sh mtx2ispan-2.sh &> mtx2ispan-2.txt & 

sh mtx2ispan-3.sh &> mtx2ispan-3.txt & 

wait

sh txt2ispan.sh &> txt2ispan.txt &

sh txt2ispan-2.sh &> txt2ispa-2.txt &

sh txt2ispan-3.sh &> txt2ispan-3.txt &

exit 0