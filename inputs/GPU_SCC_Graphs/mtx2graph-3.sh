#!/bin/bash 
 clear
./mtx2el-graph ~/inputs/mtx_graphs/cage14.mtx ~/inputs/power_law/cage14.graph
./mtx2el-graph ~/inputs/mtx_graphs/circuit5M.mtx ~/inputs/power_law/circuit5M.graph
./mtx2el-graph ~/inputs/mtx_graphs/com-Youtube.mtx ~/inputs/power_law/com-Youtube.graph
./mtx2el-graph ~/inputs/mtx_graphs/flickr.mtx ~/inputs/power_law/flickr.graph
./mtx2el-graph ~/inputs/mtx_graphs/Freescale1.mtx ~/inputs/power_law/Freescale1.graph
./mtx2el-graph ~/inputs/mtx_graphs/Freescale2.mtx ~/inputs/power_law/Freescale2.graph
./mtx2el-graph ~/inputs/mtx_graphs/soc-LiveJournal1.mtx ~/inputs/power_law/soc-LiveJournal1.graph
./mtx2el-graph ~/inputs/mtx_graphs/web-Google.mtx ~/inputs/power_law/web-Google.graph
./mtx2el-graph ~/inputs/mtx_graphs/wiki-Talk.mtx ~/inputs/power_law/wiki-Talk.graph
./mtx2el-graph ~/inputs/mtx_graphs/wikipedia-20061104.mtx ~/inputs/power_law/wikipedia-20061104.graph
exit 0