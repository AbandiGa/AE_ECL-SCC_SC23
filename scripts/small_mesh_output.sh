#!/bin/bash 
 clear

for i in {1..9}; do
    # Execute the command
    ulimit -s unlimited
    sh ECL_SCC_small_mesh.sh &> ~/SCC/output/small_mesh-"$i".txt &
    # Wait for the command to finish
    wait
done


for i in {1..9}; do
  	sh gpu_small_mesh_graphs.sh &> ~/SCC/output/GPU_small_mesh-"$i".txt &
  	wait
done


sh iSpan_small_mesh.sh &> ~/SCC/output/ispan_small_mesh.txt &
wait 

exit 0