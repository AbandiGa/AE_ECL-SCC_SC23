#!/bin/bash 
 clear
for i in {1..9}; do
    # Execute the command
    ulimit -s unlimited
    sh ECL_SCC_power_law.sh &> ~/SCC/output/power_law-"$i".txt &
    wait
done

for i in {1..9}; do
    sh gpu_power_law.sh &> ~/SCC/output/gpu_power_law-"$i".txt &
    wait
done

sh iSpan_power_law.sh &> ~/SCC/output/iSpan_power_law.txt &
wait 

exit 0