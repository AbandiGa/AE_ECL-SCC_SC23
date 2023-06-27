#!/bin/bash 
 clear
cd ~/codes/iSpan/src 
echo -e "input:cage14\n"
./ispan ~/inputs/iSpan_Graphs/power_law/ispan/cage14-fw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/cage14-fw_adjacent.bin ~/inputs/iSpan_Graphs/power_law/ispan/cage14-bw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/cage14-bw_adjacent.bin 32 30 200 10 0.01 1
echo -e "input:circuit5M\n"
./ispan ~/inputs/iSpan_Graphs/power_law/ispan/circuit5M-fw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/circuit5M-fw_adjacent.bin ~/inputs/iSpan_Graphs/power_law/ispan/circuit5M-bw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/circuit5M-bw_adjacent.bin 32 30 200 10 0.01 1
echo -e "input:com-Youtube\n"
./ispan ~/inputs/iSpan_Graphs/power_law/ispan/com-Youtube-fw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/com-Youtube-fw_adjacent.bin ~/inputs/iSpan_Graphs/power_law/ispan/com-Youtube-bw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/com-Youtube-bw_adjacent.bin 32 30 200 10 0.01 1
echo -e "input:flickr\n"
./ispan ~/inputs/iSpan_Graphs/power_law/ispan/flickr-fw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/flickr-fw_adjacent.bin ~/inputs/iSpan_Graphs/power_law/ispan/flickr-bw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/flickr-bw_adjacent.bin 32 30 200 10 0.01 1
echo -e "input:Freescale1\n"
./ispan ~/inputs/iSpan_Graphs/power_law/ispan/Freescale1-fw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/Freescale1-fw_adjacent.bin ~/inputs/iSpan_Graphs/power_law/ispan/Freescale1-bw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/Freescale1-bw_adjacent.bin 32 30 200 10 0.01 1
echo -e "input:Freescale2\n"
./ispan ~/inputs/iSpan_Graphs/power_law/ispan/Freescale2-fw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/Freescale2-fw_adjacent.bin ~/inputs/iSpan_Graphs/power_law/ispan/Freescale2-bw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/Freescale2-bw_adjacent.bin 32 30 200 10 0.01 1
echo -e "input:soc-LiveJournal1\n"
./ispan ~/inputs/iSpan_Graphs/power_law/ispan/soc-LiveJournal1-fw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/soc-LiveJournal1-fw_adjacent.bin ~/inputs/iSpan_Graphs/power_law/ispan/soc-LiveJournal1-bw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/soc-LiveJournal1-bw_adjacent.bin 32 30 200 10 0.01 1
echo -e "input:web-Google\n"
./ispan ~/inputs/iSpan_Graphs/power_law/ispan/web-Google-fw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/web-Google-fw_adjacent.bin ~/inputs/iSpan_Graphs/power_law/ispan/web-Google-bw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/web-Google-bw_adjacent.bin 32 30 200 10 0.01 1
echo -e "input:wiki-Talk\n"
./ispan ~/inputs/iSpan_Graphs/power_law/ispan/wiki-Talk-fw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/wiki-Talk-fw_adjacent.bin ~/inputs/iSpan_Graphs/power_law/ispan/wiki-Talk-bw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/wiki-Talk-bw_adjacent.bin 32 30 200 10 0.01 1
echo -e "input:wikipedia-20061104\n"
./ispan ~/inputs/iSpan_Graphs/power_law/ispan/wikipedia-20061104-fw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/wikipedia-20061104-fw_adjacent.bin ~/inputs/iSpan_Graphs/power_law/ispan/wikipedia-20061104-bw_begin.bin ~/inputs/iSpan_Graphs/power_law/ispan/wikipedia-20061104-bw_adjacent.bin 32 30 200 10 0.01 1
exit 0