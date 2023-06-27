#!/bin/bash 
 clear

Wget -P ~/SCC/inputs/mtx_graphs https://suitesparse-collection-website.herokuapp.com/MM/vanHeukelum/cage14.tar.gz

Wget -P ~/SCC/inputs/mtx_graphs https://suitesparse-collection-website.herokuapp.com/MM/Freescale/circuit5M.tar.gz

Wget -P ~/SCC/inputs/mtx_graphs  https://suitesparse-collection-website.herokuapp.com/MM/SNAP/com-Youtube.tar.gz

Wget -P ~/SCC/inputs/mtx_graphs  https://suitesparse-collection-website.herokuapp.com/MM/Gleich/flickr.tar.gz

Wget -P ~/SCC/inputs/mtx_graphs https://suitesparse-collection-website.herokuapp.com/MM/Freescale/Freescale1.tar.gz

Wget -P ~/SCC/inputs/mtx_graphs https://suitesparse-collection-website.herokuapp.com/MM/Freescale/Freescale2.tar.gz

Wget -P ~/SCC/inputs/mtx_graphs https://suitesparse-collection-website.herokuapp.com/MM/SNAP/soc-LiveJournal1.tar.gz

Wget -P ~/SCC/inputs/mtx_graphs https://suitesparse-collection-website.herokuapp.com/MM/SNAP/web-Google.tar.gz

Wget -P ~/SCC/inputs/mtx_graphs https://suitesparse-collection-website.herokuapp.com/MM/SNAP/wiki-Talk.tar.gz

Wget -P ~/SCC/inputs/mtx_graphs https://suitesparse-collection-website.herokuapp.com/MM/Gleich/wikipedia-20061104.tar.gz

tar xvzf cage14.tar.gz
cp ~/SCC/inputs/mtx_graphs/cage14/cage14.mtx cage14.mtx
tar xvzf circuit5M.tar.gz
cp ~/SCC/inputs/mtx_graphs/circuit5M/circuit5M.mtx circuit5M.mtx
tar xvzf com-Youtube.tar.gz
cp ~/SCC/inputs/mtx_graphs/com-Youtube/com-Youtube.mtx com-Youtube.mtx
tar xvzf flickr.tar.gz
cp ~/SCC/inputs/mtx_graphs/flickr/flickr.mtx flickr.mtx
tar xvzf Freescale1.tar.gz
cp ~/SCC/inputs/mtx_graphs/Freescale1/Freescale1.mtx Freescale1.mtx
tar xvzf Freescale2.tar.gz
cp ~/SCC/inputs/mtx_graphs/Freescale2/Freescale2.mtx Freescale2.mtx
tar xvzf soc-LiveJournal1.tar.gz
cp ~/SCC/inputs/mtx_graphs/soc-LiveJournal1/soc-LiveJournal1.mtx soc-LiveJournal1.mtx
tar xvzf web-Google.tar.gz
cp ~/SCC/inputs/mtx_graphs/web-Google/web-Google.mtx web-Google.mtx
tar xvzf wiki-Talk.tar.gz
cp ~/SCC/inputs/mtx_graphs/wiki-Talk/wiki-Talk.mtx wiki-Talk.mtx
tar xvzf wikipedia-20061104.tar.gz
cp ~/SCC/inputs/mtx_graphs/wikipedia-20061104/wikipedia-20061104.mtx wikipedia-20061104.mtx
exit 0