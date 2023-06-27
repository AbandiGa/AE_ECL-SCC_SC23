#include <stdlib.h>
#include <stdio.h>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <utility>
#include <tuple>
#include <algorithm>
#include <bits/stdc++.h>
#include "ECLgraph.h"

int main(int argc, char* argv[])
{
  printf("MatrixMarket to edge list(%s)\n", __FILE__);
  printf("Copyright 2016 Texas State University\n");

  if (argc != 3) {fprintf(stderr, "USAGE: %s input_file_name output_file_name\n\n", argv[0]);  exit(-1);}

  FILE* fin = fopen(argv[1], "rt");  if (fin == NULL) {fprintf(stderr, "ERROR: could not open input file %s\n\n", argv[1]);  exit(-1);}

  char line[256];
  char* ptr = line;
  size_t linesize = 256;
  int cnt = getline(&ptr, &linesize, fin);

  if (cnt < 30) {fprintf(stderr, "ERROR: could not read first line\n\n");  exit(-1);}
  if (strstr(line, "%%MatrixMarket") == 0) {fprintf(stderr, "ERROR: first line does not contain \"%%%%MatrixMarket\"\n\n");  exit(-1);}
  if (strstr(line, "matrix") == 0) {fprintf(stderr, "ERROR: first line does not contain \"matrix\"\n\n");  exit(-1);}
  if (strstr(line, "coordinate") == 0) {fprintf(stderr, "ERROR: first line does not contain \"coordinate\"\n\n");  exit(-1);}
  if ((strstr(line, "general") == 0) && (strstr(line, "symmetric") == 0)) {fprintf(stderr, "ERROR: first line does not contain \"general\" or \"symmetric\"\n\n");  exit(-1);}
  if ((strstr(line, "integer") == 0) && (strstr(line, "real") == 0) && (strstr(line, "pattern") == 0)) {fprintf(stderr, "ERROR: first line does not contain \"integer\" or \"pattern\"\n\n");  exit(-1);}
  bool hasweights = false;
  bool hasweights_r = false;
  if ((strstr(line, "integer") != 0)) hasweights = true;
  if ((strstr(line, "real") != 0)) hasweights_r = true;

  while (((cnt = getline(&ptr, &linesize, fin)) > 0) && (strstr(line, "%") != 0)) {}
  if (cnt < 3) {fprintf(stderr, "ERROR: could not find non-comment line\n\n");  exit(-1);}

  int nodes, dummy, edges;
  cnt = sscanf(line, "%d %d %d", &nodes, &dummy, &edges);
  if ((cnt != 3) || (nodes < 1) || (edges < 0) || (nodes != dummy)) {fprintf(stderr, "ERROR: failed to parse first data line\n\n");  exit(-1);}

  printf("%s\t#name\n", argv[1]);
  printf("%d\t#nodes\n", nodes);
  printf("%d\t#edges\n", edges);

  FILE* fout = fopen(argv[2], "wt");
  if (fout == NULL) {fprintf(stderr, "ERROR: could not open output file %s\n\n", argv[2]);  exit(-1);}
  fprintf(fout, "%d\t", nodes);
  fprintf(fout, "%d\n", edges);

  if ((!hasweights) && (!hasweights_r)) {
    printf("no\t#weights\n");

    int cnt = 0, src, dst;
    std::vector<std::pair<int, int>> v;
    while (fscanf(fin, "%d %d", &src, &dst) == 2) {
      cnt++;
      if ((src < 1) || (src > nodes)) {fprintf(stderr, "ERROR: source out of range\n\n");  exit(-1);}
      if ((dst < 1) || (dst > nodes)) {fprintf(stderr, "ERROR: source out of range\n\n");  exit(-1);}
      v.push_back(std::make_pair(src , dst));
    }
    fclose(fin);
    if (cnt != edges) {fprintf(stderr, "ERROR: failed to read correct number of edges\n\n");  exit(-1);}


    for (auto const& x : v) {
      fprintf(fout, "%d\t", x.first); 
      fprintf(fout, "%d", x.second);
      fprintf(fout, "\n");
    }
    
  } else if (hasweights) {
    
    int cnt = 0, src, dst, wei;
    std::vector<std::tuple<int, int, int>> v;
    while (fscanf(fin, "%d %d %d", &src, &dst, &wei) == 3) {
      cnt++;
      if ((src < 1) || (src > nodes)) {fprintf(stderr, "ERROR: source out of range\n\n");  exit(-1);}
      if ((dst < 1) || (dst > nodes)) {fprintf(stderr, "ERROR: source out of range\n\n");  exit(-1);}
      v.push_back(std::make_tuple(src, dst, wei));
    }
    fclose(fin);
    if (cnt != edges) {fprintf(stderr, "ERROR: failed to read correct number of edges\n\n");  exit(-1);}

    for (auto const& x : v) {
      fprintf(fout, "%d\t", std::get<0>(x)); 
      fprintf(fout, "%d\t", std::get<1>(x));
      //fprintf(fout, "%d\n", std::get<2>(x));
      fprintf(fout, "\n");
    }

  } else if (hasweights_r) {

    int cnt = 0, src, dst, wei;
    std::vector<std::tuple<int, int, float>> v;
    while (fscanf(fin, "%d %d %f", &src, &dst, &wei) == 3) {
      cnt++;
      if ((src < 1) || (src > nodes)) {fprintf(stderr, "ERROR: source out of range\n\n");  exit(-1);}
      if ((dst < 1) || (dst > nodes)) {fprintf(stderr, "ERROR: source out of range\n\n");  exit(-1);}
      v.push_back(std::make_tuple(src , dst, wei));
    }
    printf("cnt %d\n",cnt);
    fclose(fin);
    if (cnt != edges) {fprintf(stderr, "ERROR: failed to read correct number of edges\n\n");  exit(-1);}

    for (auto const& x : v) {
      fprintf(fout, "%d\t", std::get<0>(x)); 
      fprintf(fout, "%d", std::get<1>(x));
      //fprintf(fout, "%f\n", std::get<2>(x));
      fprintf(fout, "\n");
    }


  }

  fclose(fout);
  return 0;

 } 

