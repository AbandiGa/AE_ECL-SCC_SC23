#!/bin/bash 
python3 ~/SCC/scripts/create_dir.py
unzip ~/SCC/input/ECL_graphs/power_law.zip
unzip ~/SCC/input/mtx_graphs.zip

sh ~/SCC/scripts/get_mesh_graphs.sh &> ~/SCC/scripts/get_mesh_graphs.txt &

sh ~/SCC/scripts/get_power_law.sh &>  ~/SCC/scripts/get_power_law.txt &

chmod +x install_python3.sh
./install_python3.sh

wait

python ~/SCC/scripts/run_all.py 


exit 0 
