#!/bin/bash 
 clear

sh get_small_mesh.sh &> get_small_mesh.txt &

sh get_large_mesh.sh &> get_large_mesh.txt &

exit 0