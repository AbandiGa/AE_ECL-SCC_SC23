#!/bin/bash 
 clear

for i in {1..9}; do
    # Execute the command
    ulimit -s unlimited
    sh ECL_SCC_large_mesh_graphs.sh &> ~/SCC/output/large_mesh-"$i".txt &
    # Wait for the command to finish
    wait
done


for i in {1..9}; do
    sh gpu_large_mesh_graphs.sh &> ~/SCC/output/GPU_large_mesh-"$i".txt &
    wait
done


sh iSpan_large_mesh.sh &> ~/SCC/output/ispan_large_mesh.txt &
wait 

exit 0