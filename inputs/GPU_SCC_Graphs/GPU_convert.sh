#!/bin/bash 
 clear

sh mtx2graph.sh &> mtx2graph.txt &

sh mtx2graph-2.sh &> mtx2graph-2.txt &

sh mtx2graph-3.sh &> mtx2graph-3.txt &

exit 0