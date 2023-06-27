
import re
from openpyxl import Workbook
import time
import collections

'''
f = open('klein-67.txt', 'r')
lines = f.readlines()
f.close()

'''
def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None

book = Workbook()
sheet = book.active
sheet['A1'] = "Graph"
sheet['B1'] = "MP-SCC"
sheet['C1'] = "GPU-SCC"
sheet['D1'] = "iSpan"

Graphs1 = ['flickr', 'soc-LiveJournal1', 'web-Google', 'wikipedia-20070206']
Graphs2 = ['beam-hex.mesh-M-4-idx-0.egr',
'beam-hex.mesh-M-4-idx-1.egr',
'beam-hex.mesh-M-4-idx-2.egr',
'beam-hex.mesh-M-4-idx-3.egr',
'beam-hex.mesh-M-4-idx-4.egr',
'beam-hex.mesh-M-4-idx-5.egr', 
'beam-hex.mesh-M-4-idx-6.egr',
'beam-hex.mesh-M-4-idx-7.egr',
'beam-hex.mesh-M-4-idx-3.egr',
'beam-hex.mesh-M-4-idx-8.egr',
'beam-hex.mesh-M-4-idx-9.egr',    
'beam-hex.mesh-M-4-idx-10.egr',  
'beam-hex.mesh-M-4-idx-11.egr',  
'beam-hex.mesh-M-4-idx-12.egr',  
'beam-hex.mesh-M-4-idx-13.egr',  
'beam-hex.mesh-M-4-idx-14.egr',  
'beam-hex.mesh-M-4-idx-15.egr', 
'beam-hex.mesh-M-4-idx-16.egr',  
'beam-hex.mesh-M-4-idx-17.egr',  
'beam-hex.mesh-M-4-idx-18.egr',  
'beam-hex.mesh-M-4-idx-19.egr',    
'beam-hex.mesh-M-4-idx-20.egr',  
'beam-hex.mesh-M-4-idx-21.egr',  
'beam-hex.mesh-M-4-idx-22.egr',  
'beam-hex.mesh-M-4-idx-23.egr',
'beam-hex.mesh-M-4-idx-24.egr',  
'beam-hex.mesh-M-4-idx-25.egr',
'beam-hex.mesh-M-4-idx-26.egr',  
'beam-hex.mesh-M-4-idx-27.egr',
'beam-hex.mesh-M-4-idx-28.egr',
'star.mesh-M-4-idx-0.egr',
'star.mesh-M-4-idx-1.egr',
'star.mesh-M-4-idx-2.egr',
'star.mesh-M-4-idx-3.egr',
'star.mesh-M-4-idx-4.egr',
'star.mesh-M-4-idx-5.egr',
'star.mesh-M-4-idx-6.egr',
'star.mesh-M-4-idx-7.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-0.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-10.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-11.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-12.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-13.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-14.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-15.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-16.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-17.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-18.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-19.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-1.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-20.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-21.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-22.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-23.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-24.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-25.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-26.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-27.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-28.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-29.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-2.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-30.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-31.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-3.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-4.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-5.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-6.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-7.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-8.egr',
'cold-flow-sponge-tao4-r2.msh-M-4-idx-9.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-0.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-10.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-11.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-12.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-13.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-14.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-15.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-16.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-17.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-18.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-19.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-1.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-20.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-21.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-22.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-23.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-24.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-25.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-26.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-27.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-28.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-29.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-2.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-30.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-31.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-3.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-4.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-5.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-6.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-7.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-8.egr',
'cold-flow-spongezone3.c1.msh-M-4-idx-9.egr',
'toroid-hex.mesh-M-4-idx-0.egr',
'toroid-hex.mesh-M-4-idx-1.egr',
'toroid-hex.mesh-M-4-idx-2.egr',
'toroid-hex.mesh-M-4-idx-3.egr',
'toroid-hex.mesh-M-4-idx-4.egr',
'toroid-hex.mesh-M-4-idx-5.egr',
'toroid-hex.mesh-M-4-idx-6.egr',
'toroid-hex.mesh-M-4-idx-7.egr',
'toroid-hex.mesh-M-4-idx-8.egr',
'toroid-hex.mesh-M-4-idx-9.egr',
'toroid-hex.mesh-M-4-idx-10.egr',
'toroid-hex.mesh-M-4-idx-11.egr',
'toroid-hex.mesh-M-4-idx-12.egr',
'toroid-hex.mesh-M-4-idx-13.egr',
'toroid-hex.mesh-M-4-idx-14.egr',
'toroid-hex.mesh-M-4-idx-15.egr',
'toroid-hex.mesh-M-4-idx-16.egr',
'toroid-hex.mesh-M-4-idx-17.egr',
'toroid-hex.mesh-M-4-idx-18.egr',
'toroid-hex.mesh-M-4-idx-19.egr',
'toroid-hex.mesh-M-4-idx-20.egr',
'toroid-hex.mesh-M-4-idx-21.egr',
'toroid-hex.mesh-M-4-idx-22.egr',
'toroid-hex.mesh-M-4-idx-23.egr',
'toroid-hex.mesh-M-4-idx-24.egr',
'toroid-hex.mesh-M-4-idx-25.egr',
'toroid-hex.mesh-M-4-idx-26.egr',
'toroid-hex.mesh-M-4-idx-27.egr',
'toroid-hex.mesh-M-4-idx-28.egr',
'toroid-hex.mesh-M-4-idx-29.egr',
'toroid-hex.mesh-M-4-idx-30.egr',
'toroid-hex.mesh-M-4-idx-31.egr',
'toroid-wedge.mesh-M-4-idx-0.egr',
'toroid-wedge.mesh-M-4-idx-1.egr',
'toroid-wedge.mesh-M-4-idx-2.egr',
'toroid-wedge.mesh-M-4-idx-3.egr',
'toroid-wedge.mesh-M-4-idx-4.egr',
'toroid-wedge.mesh-M-4-idx-5.egr',
'toroid-wedge.mesh-M-4-idx-6.egr',
'toroid-wedge.mesh-M-4-idx-7.egr',
'toroid-wedge.mesh-M-4-idx-8.egr',
'toroid-wedge.mesh-M-4-idx-9.egr',
'toroid-wedge.mesh-M-4-idx-10.egr',
'toroid-wedge.mesh-M-4-idx-11.egr',
'toroid-wedge.mesh-M-4-idx-12.egr',
'toroid-wedge.mesh-M-4-idx-13.egr',
'toroid-wedge.mesh-M-4-idx-14.egr',
'toroid-wedge.mesh-M-4-idx-15.egr',
'toroid-wedge.mesh-M-4-idx-16.egr',
'toroid-wedge.mesh-M-4-idx-17.egr',
'toroid-wedge.mesh-M-4-idx-18.egr',
'toroid-wedge.mesh-M-4-idx-19.egr',
'toroid-wedge.mesh-M-4-idx-20.egr',
'toroid-wedge.mesh-M-4-idx-21.egr',
'toroid-wedge.mesh-M-4-idx-22.egr',
'toroid-wedge.mesh-M-4-idx-23.egr',
'toroid-wedge.mesh-M-4-idx-24.egr',
'toroid-wedge.mesh-M-4-idx-25.egr',
'toroid-wedge.mesh-M-4-idx-26.egr',
'toroid-wedge.mesh-M-4-idx-27.egr',
'toroid-wedge.mesh-M-4-idx-28.egr',
'toroid-wedge.mesh-M-4-idx-29.egr',
'toroid-wedge.mesh-M-4-idx-30.egr',
'toroid-wedge.mesh-M-4-idx-31.egr']

MP_files = ['larger_mesh-1.txt','larger_mesh-2.txt','larger_mesh-3.txt','larger_mesh-4.txt',
'larger_mesh-5.txt','larger_mesh-6.txt','larger_mesh-7.txt','larger_mesh-8.txt','larger_mesh-9.txt']
GPU_files = ['GPU_larger_mesh-1.txt','GPU_larger_mesh-2.txt','GPU_larger_mesh-3.txt','GPU_larger_mesh-4.txt',
'GPU_larger_mesh-5.txt','GPU_larger_mesh-6.txt','GPU_larger_mesh-7.txt','GPU_larger_mesh-8.txt','GPU_larger_mesh-9.txt']
#ispan_files = ['ispan_larger_mesh-1.txt','ispan_larger_mesh-2.txt','ispan_larger_mesh-3.txt','ispan_larger_mesh-4.txt',
#'ispan_larger_mesh-5.txt','ispan_larger_mesh-6.txt','ispan_larger_mesh-7.txt','ispan_larger_mesh-8.txt','ispan_larger_mesh-9.txt']

all_files = []
all_files.append(MP_files)
all_files.append(GPU_files)

codes = ['B', 'C']
c = 0;
nodes = []

for files in all_files:
    cell = ['I','J','K','L','M','N','O','P','Q']
    cell2 =['R','S','T','U','V','W','X','Y','Z']
    cell3 = ['AA','AB','AC','AD','AE','AF','AG','AH','AI']
    info = {}

    for fi in files:
        f = open(fi, 'r')
        lines = f.readlines()
        f.close()  
        j = 2

        for i, line in enumerate(lines):
           
            if "input: /home/gaa54/larger_mesh_all/" in line:
                text="input: /home/gaa54/larger_mesh_all/(.*)"
                m = re.search(text,lines[i])
                graph = str(m.group(1).split('.egr')[0])
                if graph not in info:
                    info.setdefault(graph,[])
            elif "input:" in line:
                text="input:(.+)"
                m = re.search(text, lines[i])
                graph = str(m.group(1))
                if graph not in info:
                    info.setdefault(graph,[])
            elif "nodes:" in line:
                text="nodes: (.+)"
                m = re.search(text,lines[i])
                nodes.append(int(m.group(1)))
            elif "ECL-SCC compute time:" in line:
                text="ECL-SCC compute time: (.+) s"
                m = re.search(text, lines[i])
                info[graph].append(float(m.group(1))) 
                j+=1
            elif "time:" in line:
                text="time: (.+)"
                m = re.search(text, lines[i])
                gpu_time = m.group(1).split('s')[0]
                info[graph].append(float(gpu_time)) 
                j+=1 

    avg_runtime =[]
    avg_runtime.append(-1)
    for graph in info:
        info[graph].sort()
        #print(info[graph])
        mid = len(info[graph]) // 2
        time = (info[graph][mid] + info[graph][~mid]) / 2
        avg_runtime.append(time)



    start = [1, 33, 65, 73, 81, 113, 145]
    end = [32, 64, 72, 80, 112, 144, 205]

    graphs =["torch-hex", "torch-tet", "klein-bottle", "mobius-strip.", "toroid-hex", "toroid-wedge", "twist-hex"]
    j = 2
    t = 0
    for g in graphs:
        sheet['A'+str(j)] = g
        beg = start[t]
        end_idx = end[t]+1
        avg = sum(avg_runtime[beg:end_idx])/len(avg_runtime[beg:end_idx])
        #print(g+" , "+str(avg))
        throughput = nodes[beg]/avg/1000000
        #print(g+" , "+str(throughput))
        sheet[codes[c]+str(j)] =  throughput
        t += 1
        j += 1
    c += 1


ispan_files = ['ispan_larger_mesh.txt']

#['ispan_larger_mesh-1.txt','ispan_larger_mesh-2.txt','ispan_larger_mesh-3.txt','ispan_larger_mesh-4.txt',
#'ispan_larger_mesh-5.txt','ispan_larger_mesh-6.txt','ispan_larger_mesh-7.txt','ispan_larger_mesh-8.txt','ispan_larger_mesh-9.txt']

info = {}
for file in ispan_files:
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    j = 1;

    for i, line in enumerate(lines):  
        if "input:" in line:
            j+=1
            text="input:(.+)"
            m = re.search(text, lines[i])
            graph = str(m.group(1))
            if graph not in info:
                info.setdefault(graph,[])
        elif "total time," in line:
            text="total time, (.+)"
            m = re.search(text, lines[i])
            ispan_time = float(m.group(1))
            info[graph].append(float(ispan_time)* 0.001) 


    avg_runtime =[]
    avg_runtime.append(-1)
    for graph in info:
        print(graph,info[graph])
        info[graph].sort()
        if not info[graph]:
           avg_runtime.append(0) 
        else:
            mid = len(info[graph]) // 2
            time = (info[graph][mid] + info[graph][~mid]) / 2
            avg_runtime.append(time)

    start = [1, 33, 65, 73, 81, 113, 145]
    end = [32, 64, 72, 80, 112, 144, 205]

    graphs =["torch-hex", "torch-tet", "klein-bottle", "mobius-strip.", "toroid-hex", "toroid-wedge", "twist-hex"]
    j = 2
    t = 0
    for g in graphs:
        sheet['A'+str(j)] = g
        beg = start[t]
        end_idx = end[t]+1
        avg = sum(avg_runtime[beg:end_idx])/len(avg_runtime[beg:end_idx])
        print(g+" , "+str(avg))
        throughput = nodes[beg]/avg/1000000
        print(g+" , "+str(throughput))
        sheet['D'+str(j)] =  throughput
        t += 1
        j += 1
        

book.save("Large_mesh.xlsx") 


###################################################################################################

MP_files = ['small_mesh-1.txt','small_mesh-2.txt','small_mesh-3.txt','small_mesh-4.txt',
'small_mesh-5.txt','small_mesh-6.txt','small_mesh-7.txt','small_mesh-8.txt','small_mesh-9.txt']
GPU_files = ['GPU_small_mesh-1.txt','GPU_small_mesh-2.txt','GPU_small_mesh-3.txt','GPU_small_mesh-4.txt',
'GPU_small_mesh-5.txt','GPU_small_mesh-6.txt','GPU_small_mesh-7.txt','GPU_small_mesh-8.txt','GPU_small_mesh-9.txt']


all_small_files = []
all_small_files.append(MP_files)
all_small_files.append(GPU_files)

codes = ['B', 'C']
c = 0;
nodes = []

for files in all_small_files:
    cell = ['I','J','K','L','M','N','O','P','Q']
    cell2 =['R','S','T','U','V','W','X','Y','Z']
    cell3 = ['AA','AB','AC','AD','AE','AF','AG','AH','AI']
    info = {}

    for fi in files:
        f = open(fi, 'r')
        lines = f.readlines()
        f.close()  
        j = 2

        for i, line in enumerate(lines):
           
            if "input: /home/gaa54/larger_mesh_all/" in line:
                text="input: /home/gaa54/larger_mesh_all/(.*)"
                m = re.search(text,lines[i])
                graph = str(m.group(1).split('.egr')[0])
                if graph not in info:
                    info.setdefault(graph,[])
            elif "input:" in line:
                text="input:(.+)"
                m = re.search(text, lines[i])
                graph = str(m.group(1))
                if graph not in info:
                    info.setdefault(graph,[])
            elif "nodes:" in line:
                text="nodes: (.+)"
                m = re.search(text,lines[i])
                nodes.append(int(m.group(1)))
            elif "ECL-SCC compute time:" in line:
                text="ECL-SCC compute time: (.+) s"
                m = re.search(text, lines[i])
                info[graph].append(float(m.group(1))) 
                j+=1
            elif "time:" in line:
                text="time: (.+)"
                m = re.search(text, lines[i])
                gpu_time = m.group(1).split('s')[0]
                info[graph].append(float(gpu_time)) 
                j+=1 

    avg_runtime =[]
    avg_runtime.append(-1)
    for graph in info:
        info[graph].sort()
        #print(info[graph])
        mid = len(info[graph]) // 2
        time = (info[graph][mid] + info[graph][~mid]) / 2
        avg_runtime.append(time)



    start = [1, 35, 63, 94, 103, 135]
    end = [30, 62, 93, 102, 134, 166]

    graphs =["beam-hex", "torch-hex", "torch-tet", "star_mesh", "toroid-hex", "toroid-wedge"]    j = 2
    t = 0
    for g in graphs:
        sheet['A'+str(j)] = g
        beg = start[t]
        end_idx = end[t]+1
        avg = sum(avg_runtime[beg:end_idx])/len(avg_runtime[beg:end_idx])
        #print(g+" , "+str(avg))
        throughput = nodes[beg]/avg/1000000
        #print(g+" , "+str(throughput))
        sheet[codes[c]+str(j)] =  throughput
        t += 1
        j += 1
    c += 1


ispan_files = ['ispan_small_mesh.txt']

info = {}
for file in ispan_files:
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    j = 1;

    for i, line in enumerate(lines):  
        if "input:" in line:
            j+=1
            text="input:(.+)"
            m = re.search(text, lines[i])
            graph = str(m.group(1))
            if graph not in info:
                info.setdefault(graph,[])
        elif "total time," in line:
            text="total time, (.+)"
            m = re.search(text, lines[i])
            ispan_time = float(m.group(1))
            info[graph].append(float(ispan_time)* 0.001) 

    print("iSpan")
    avg_runtime =[]
    avg_runtime.append(-1)
    for graph in info:
        print(graph,info[graph])
        info[graph].sort()
        if not info[graph]:
           avg_runtime.append(0) 
        else:
            mid = len(info[graph]) // 2
            time = (info[graph][mid] + info[graph][~mid]) / 2
            avg_runtime.append(time)

    start = [1, 35, 63, 94, 103, 135]
    end = [30, 62, 93, 102, 134, 166]

    graphs =["beam-hex", "torch-hex", "torch-tet", "star_mesh", "toroid-hex", "toroid-wedge"]
    j = 2
    t = 0
    for g in graphs:
        sheet['A'+str(j)] = g
        beg = start[t]
        end_idx = end[t]+1
        avg = sum(avg_runtime[beg:end_idx])/len(avg_runtime[beg:end_idx])
        print(g+" , "+str(avg))
        throughput = nodes[beg]/avg/1000000
        print(g+" , "+str(throughput))
        sheet['D'+str(j)] =  throughput
        t += 1
        j += 1
        

book.save("small_mesh.xlsx") 

###################################################################################################

MP_files = ['power_law-1.txt','power_law-2.txt','power_law-3.txt','power_law-4.txt',
'power_law-5.txt','power_law-6.txt','power_law-7.txt','power_law-8.txt','power_law-9.txt']
GPU_files = ['GPU_power_law-1.txt','GPU_power_law-2.txt','GPU_power_law-3.txt','GPU_power_law-4.txt',
'GPU_power_law-5.txt','GPU_power_law-6.txt','GPU_power_law-7.txt','GPU_power_law-8.txt','GPU_power_law-9.txt']


all_small_files = []
all_small_files.append(MP_files)
all_small_files.append(GPU_files)

codes = ['B', 'C']
c = 0;
nodes = []

for files in all_small_files:
    cell = ['I','J','K','L','M','N','O','P','Q']
    cell2 =['R','S','T','U','V','W','X','Y','Z']
    cell3 = ['AA','AB','AC','AD','AE','AF','AG','AH','AI']
    info = {}

    for fi in files:
        f = open(fi, 'r')
        lines = f.readlines()
        f.close()  
        j = 2

        for i, line in enumerate(lines):
           
            if "input: /home/gaa54/larger_mesh_all/" in line:
                text="input: /home/gaa54/larger_mesh_all/(.*)"
                m = re.search(text,lines[i])
                graph = str(m.group(1).split('.egr')[0])
                if graph not in info:
                    info.setdefault(graph,[])
            elif "input:" in line:
                text="input:(.+)"
                m = re.search(text, lines[i])
                graph = str(m.group(1))
                if graph not in info:
                    info.setdefault(graph,[])
            elif "nodes:" in line:
                text="nodes: (.+)"
                m = re.search(text,lines[i])
                nodes.append(int(m.group(1)))
            elif "ECL-SCC compute time:" in line:
                text="ECL-SCC compute time: (.+) s"
                m = re.search(text, lines[i])
                info[graph].append(float(m.group(1))) 
            elif "time:" in line:
                text="time: (.+)"
                m = re.search(text, lines[i])
                gpu_time = m.group(1).split('s')[0]
                info[graph].append(float(gpu_time)) 


    avg_runtime =[]
    avg_runtime.append(-1)
    n = 0

    for graph in info:
        sheet['A'+str(j)] = graph
        mid = len(info[graph]) // 2
        time = (info[graph][mid] + info[graph][~mid]) / 2
        avg_runtime.append(time)
        throughput = nodes[n]/time/1000000
        sheet[codes[c]+str(j)] =  throughput
        j += 1
        n += 1


ispan_files = ['ispan_power_law.txt']

info = {}
for file in ispan_files:
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    j = 1;

    for i, line in enumerate(lines):  
        if "input:" in line:
            j+=1
            text="input:(.+)"
            m = re.search(text, lines[i])
            graph = str(m.group(1))
            if graph not in info:
                info.setdefault(graph,[])
        elif "total time," in line:
            text="total time, (.+)"
            m = re.search(text, lines[i])
            ispan_time = float(m.group(1))
            info[graph].append(float(ispan_time)* 0.001) 


    avg_runtime =[]
    avg_runtime.append(-1)
    n = 0
    for graph in info:
        sheet['A'+str(j)] = graph
        if not info[graph]:
           avg_runtime.append(0) 
        else:
            sheet['A'+str(j)] = graph
            mid = len(info[graph]) // 2
            time = (info[graph][mid] + info[graph][~mid]) / 2
            avg_runtime.append(time)
            throughput = nodes[n]/time/1000000
            sheet[codes[c]+str(j)] =  throughput
        j += 1
        n += 1

    
        

book.save("power_law.xlsx") 
