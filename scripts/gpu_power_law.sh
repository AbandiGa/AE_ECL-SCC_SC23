#!/bin/bash 
 clear
cd ~/codes/gpuscc_code
echo -e "input:cage14\n"
./scc_2_w -f ~/inputs/GPU_SCC_Graphs/power_law/cage14.graph
echo -e "input:circuit5M\n"
./scc_2_w -f ~/inputs/GPU_SCC_Graphs/power_law/circuit5M.graph
echo -e "input:com-Youtube\n"
./scc_2_w -f ~/inputs/GPU_SCC_Graphs/power_law/com-Youtube.graph
echo -e "input:flickr\n"
./scc_2_w -f ~/inputs/GPU_SCC_Graphs/power_law/flickr.graph
echo -e "input:Freescale1\n"
./scc_2_w -f ~/inputs/GPU_SCC_Graphs/power_law/Freescale1.graph
echo -e "input:Freescale2\n"
./scc_2_w -f ~/inputs/GPU_SCC_Graphs/power_law/Freescale2.graph
echo -e "input:soc-LiveJournal1\n"
./scc_2_w -f ~/inputs/GPU_SCC_Graphs/power_law/soc-LiveJournal1.graph
echo -e "input:web-Google\n"
./scc_2_w -f ~/inputs/GPU_SCC_Graphs/power_law/web-Google.graph
echo -e "input:wiki-Talk\n"
./scc_2_w -f ~/inputs/GPU_SCC_Graphs/power_law/wiki-Talk.graph
echo -e "input:wikipedia-20061104\n"
./scc_2_w -f ~/inputs/GPU_SCC_Graphs/power_law/wikipedia-20061104.graph
exit 0