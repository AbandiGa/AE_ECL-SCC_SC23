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

    source_file_ECL = "ECL-SCC.cu"
    output_file_ECL = "ecl-scc"
    compiler_command = f"nvcc -O3 -arch=sm_70 {ECL_code_path}/{output_file_ECL} -o {output_file_ECL}"
    os.system(compiler_command)
   

    source_file_mtx = "mtx_convert.cpp"
    output_file_mtx = "ecl2mtx"
    compiler_command = f"g++ {mtx_file_path}/{source_file_mtx} -o {output_file_mtx}"
    os.system(compiler_command)

    compiler_command = f"g++ {mtx_file_path}/mtx2ecl.cpp -o {mtx2ecl}"
    os.system(compiler_command)


    source_file_gpu = "mtx2graph.cpp"
    output_file_gpu = "mtx2el-graph"
    compiler_command = f"g++ {GPU_file_path}/{source_file_gpu} -o {output_file_gpu}"
    os.system(compiler_command)

    source_file_ispan = "mtx2iSpan.cpp"
    output_file_ipsan = "mtx2el-iSpan"
    compiler_command = f"g++ {iSpan_file_path}/{source_file_ispan} -o {output_file_ipsan}"
    os.system(compiler_command)

    source_file_fw = "txt_to_bin_fw_int.cpp"
    output_file_fw = "txt_to_bin_fw"
    compiler_command = f"g++ {GPU_file_path}/{source_file_fw} -o {output_file_fw}"
    os.system(compiler_command)
    
    source_file_bw = "txt_to_bin_bw_int.cpp"
    output_file_bw = "txt_to_bin_bw"
    compiler_command = f"g++ {GPU_file_path}/{source_file_bw} -o {output_file_bw}"
    os.system(compiler_command)

    compiler_command = f"sh {mtx_file_path}/mtx_convert.sh &> {mtx_file_path}/mtx_convert.txt & wait"
    os.system(compiler_command)
    compiler_command = f"sh {mtx_file_path}/mtx2ecl.sh &> {mtx_file_path}/mtx2ecl.txt & wait"
    os.system(compiler_command)
    compiler_command = f"sh {GPU_file_path}/GPUconvert.sh &> {GPU_file_path}/GPU_convert.txt & wait"
    os.system(compiler_command)
    compiler_command = f"sh {iSpan_file_path}/iSpan_Graphs.sh &> {iSpan_file_path}/iSpan_Graphs.txt & wait"
    os.system(compiler_command)

    os.system("sh power_law_output.sh &> power_law_output.txt & wait")
    os.system("sh Large_mesh_output.sh &> Large_mesh_output.txt & wait")
    os.system("sh small_mesh_output.sh &> small_mesh_output.txt & wait")


    os.system("python3 generate_xlsx.py")
    os.system("python3 generate_garphs.py")
            