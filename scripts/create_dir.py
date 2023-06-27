#!/usr/bin/python3 -u

import os
import sys


# Get the home directory
home_dir = os.path.expanduser("~")
code_path =  os.path.join(home_dir,'/SCC/codes/')
mtx_file_path = os.path.join(home_dir,'/SCC/inputs/mtx_graphs/')
ECL_file_path = os.path.join(home_dir,'/SCC/inputs/ECL_graphs/')
GPU_file_path = os.path.join(home_dir,'/SCC/inputs/GPU_SCC_Graphs/')
iSpan_file_path = os.path.join(home_dir,'/SCC/inputs/iSpan_Graphs/')
ECL_code_path = os.path.join(home_dir,'/SCC/codes/ECL_SCC/')


if __name__ == "__main__":

    if os.path.exists('output/'):
        os.system('rm -rf %s' % ('output/'))
    os.mkdir('output/')

    if os.path.exists('inputs/ECL_graphs/small_mesh_graphs'):
        os.system('rm -rf %s' % ('inputs/ECL_graphs/small_mesh_graphs'))
    os.mkdir('inputs/ECL_graphs/small_mesh_graphs')

    if os.path.exists('inputs/ECL_graphs/large_mesh_graphs'):
        os.system('rm -rf %s' % ('inputs/ECL_graphs/large_mesh_graphs'))
    os.mkdir('inputs/ECL_graphs/large_mesh_graphs')
    
    if os.path.exists('inputs/ECL_graphs/power_law'):
        os.system('rm -rf %s' % ('inputs/ECL_graphs/power_law'))
    os.mkdir('inputs/ECL_graphs/power_law')


    if os.path.exists('inputs/GPU_SCC_Graphs/small_mesh_graphs'):
        os.system('rm -rf %s' % ('inputs/GPU_SCC_Graphs/small_mesh_graphs'))
    os.mkdir('inputs/GPU_SCC_Graphs/small_mesh_graphs')

    if os.path.exists('inputs/GPU_SCC_Graphs/large_mesh_graphs'):
        os.system('rm -rf %s' % ('inputs/GPU_SCC_Graphs/large_mesh_graphs'))
    os.mkdir('inputs/GPU_SCC_Graphs/large_mesh_graphs')
    
    if os.path.exists('inputs/GPU_SCC_Graphs/power_law'):
        os.system('rm -rf %s' % ('inputs/GPU_SCC_Graphs/power_law'))
    os.mkdir('inputs/GPU_SCC_Graphs/power_law')

    if os.path.exists('inputs/iSpan_Graphs/small_mesh_graphs'):
        os.system('rm -rf %s' % ('inputs/iSpan_Graphs/small_mesh_graphs'))
    os.mkdir('inputs/iSpan_Graphs/small_mesh_graphs')

    if os.path.exists('inputs/iSpan_Graphs/large_mesh_graphs'):
        os.system('rm -rf %s' % ('inputs/iSpan_Graphs/large_mesh_graphs'))
    os.mkdir('inputs/iSpan_Graphs/large_mesh_graphs')
    
    if os.path.exists('inputs/iSpan_Graphs/power_law'):
        os.system('rm -rf %s' % ('inputs/iSpan_Graphs/power_law'))
    os.mkdir('inputs/iSpan_Graphs/power_law')

