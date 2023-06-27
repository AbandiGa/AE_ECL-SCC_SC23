#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <utility>
#include <tuple>
#include <algorithm>
#include <bits/stdc++.h>
#include "ECLgraph.h"

static bool sortbysec(const std::pair<int, int>& a, const std::pair<int, int>& b)
{
  return (a.second < b.second) || ((a.second == b.second) && (a.first < b.first));
}

static bool sortweibysec(const std::tuple<int, int, int>& a, const std::tuple<int, int, int>& b)
{
  return (std::get<1>(a) < std::get<1>(b)) || ((std::get<1>(a) == std::get<1>(b)) && (std::get<0>(a) < std::get<0>(b)));
}

int main(int argc, char* argv [])
{
  printf("MatrixMarket to dual ECL Graph Converter (%s)\n", __FILE__);
  printf("Copyright 2022 Texas State University\n");

  if (argc != 4) {fprintf(stderr, "USAGE: %s input_file_name output_in_file_name output_out_file_name\n\n", argv[0]);  exit(-1);}

  FILE* fin = fopen(argv[1], "rt");  if (fin == NULL) {fprintf(stderr, "ERROR: could not open input file %s\n\n", argv[1]);  exit(-1);}

  char line [256];
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
  if (strstr(line, "integer") != 0) hasweights = true;

  bool hasweights_r = false;
  if (strstr(line, "real") != 0) hasweights_r = true;

  while (((cnt = getline(&ptr, &linesize, fin)) > 0) && (strstr(line, "%") != 0)) {}
  if (cnt < 3) {fprintf(stderr, "ERROR: could not find non-comment line\n\n");  exit(-1);}

  int nodes, dummy, edges;
  cnt = sscanf(line, "%d %d %d", &nodes, &dummy, &edges);
  if ((cnt != 3) || (nodes < 1) || (edges < 0) || (nodes != dummy)) {fprintf(stderr, "ERROR: failed to parse first data line\n\n");  exit(-1);}

  printf("%s\t#name\n", argv[1]);
  printf("%d\t#nodes\n", nodes);
  printf("%d\t#edges\n", edges);

  ECLgraph gin;
  gin.nodes = nodes;
  gin.edges = edges;
  gin.nindex = (int*)calloc(nodes + 1, sizeof(int));
  gin.nlist = (int*)malloc(edges * sizeof(int));
  gin.eweight = NULL;
  ECLgraph gout;
  gout.nodes = nodes;
  gout.edges = edges;
  gout.nindex = (int*)calloc(nodes + 1, sizeof(int));
  gout.nlist = (int*)malloc(edges * sizeof(int));
  gout.eweight = NULL;
  if ((gin.nindex == NULL) || (gin.nlist == NULL)) {fprintf(stderr, "ERROR: memory allocation failed\n\n");  exit(-1);}
  if ((gout.nindex == NULL) || (gout.nlist == NULL)) {fprintf(stderr, "ERROR: memory allocation failed\n\n");  exit(-1);}

  if ((!hasweights) && (!hasweights_r)) {
    printf("no\t#weights\n");

    int cnt = 0, src, dst;
    std::vector<std::pair<int, int>> v;
    while (fscanf(fin, "%d %d", &src, &dst) == 2) {
      cnt++;
      if ((src < 1) || (src > nodes)) {fprintf(stderr, "ERROR: source out of range\n\n");  exit(-1);}
      if ((dst < 1) || (dst > nodes)) {fprintf(stderr, "ERROR: source out of range\n\n");  exit(-1);}
      v.push_back(std::make_pair(src - 1, dst - 1));
      printf("%d %d\n",src, dst);
    }
    fclose(fin);
    if (cnt != edges) {fprintf(stderr, "ERROR: failed to read correct number of edges\n\n");  exit(-1);}

    std::sort(v.begin(), v.end());

    gout.nindex[0] = 0;
    for (int i = 0; i < edges; i++) {
      int src = v[i].first;
      int dst = v[i].second;
      gout.nindex[src + 1] = i + 1;
      gout.nlist[i] = dst;
    }

    std::sort(v.begin(), v.end(), sortbysec);

    gin.nindex[0] = 0;
    for (int i = 0; i < edges; i++) {
      int src = v[i].first;
      int dst = v[i].second;
      gin.nindex[dst + 1] = i + 1;
      gin.nlist[i] = src;
    }
  } else if (hasweights) {
    printf("yes\t#weights\n");

    gout.eweight = (int*)malloc(edges * sizeof(int));
    if (gout.eweight == NULL) {fprintf(stderr, "ERROR: memory allocation failed\n\n");  exit(-1);}

    gin.eweight = (int*)malloc(edges * sizeof(int));
    if (gin.eweight == NULL) {fprintf(stderr, "ERROR: memory allocation failed\n\n");  exit(-1);}
  
    int cnt = 0, src, dst, wei;

    std::vector<std::tuple<int, int, int>> v;
    while (fscanf(fin, "%d %d %d", &src, &dst, &wei) == 3) {
      cnt++;
      if ((src < 1) || (src > nodes)) {fprintf(stderr, "ERROR: source out of range\n\n");  exit(-1);}
      if ((dst < 1) || (dst > nodes)) {fprintf(stderr, "ERROR: source out of range\n\n");  exit(-1);}
      v.push_back(std::make_tuple(src - 1, dst - 1, wei));
    }
    fclose(fin);
    if (cnt != edges) {fprintf(stderr, "ERROR: failed to read correct number of edges\n\n");  exit(-1);}

    std::sort(v.begin(), v.end());

    gout.nindex[0] = 0;
    for (int i = 0; i < edges; i++) {
      int src = std::get<0>(v[i]);
      int dst = std::get<1>(v[i]);
      int wei = std::get<2>(v[i]);
      gout.nindex[src + 1] = i + 1;
      gout.nlist[i] = dst;
      gout.eweight[i] = wei;
    }

    std::sort(v.begin(), v.end(), sortweibysec);

    gin.nindex[0] = 0;
    for (int i = 0; i < edges; i++) {
      int src = std::get<0>(v[i]);
      int dst = std::get<1>(v[i]);
      int wei = std::get<2>(v[i]);
      gin.nindex[dst + 1] = i + 1;
      gin.nlist[i] = src;
      gin.eweight[i] = wei;
    }
  }else if (hasweights_r) {
    printf("real weights\n"); 
    int cnt = 0, src, dst;
    float wei;
    std::vector<std::pair<int, int>> v;
    while (fscanf(fin, "%d %d %f", &src, &dst, &wei) == 3) {
      cnt++;
      if ((src < 1) || (src > nodes)) {fprintf(stderr, "ERROR: source out of range\n\n");  exit(-1);}
      if ((dst < 1) || (dst > nodes)) {fprintf(stderr, "ERROR: source out of range\n\n");  exit(-1);}
      v.push_back(std::make_pair(src - 1, dst - 1));
      //printf("%d %d %f\n",src, dst, wei);
    }
    fclose(fin);
    if (cnt != edges) {fprintf(stderr, "ERROR: failed to read correct number of edges\n\n");  exit(-1);}

    std::sort(v.begin(), v.end());

    gout.nindex[0] = 0;
    for (int i = 0; i < edges; i++) {
      int src = std::get<0>(v[i]);
      int dst = std::get<1>(v[i]);
      gout.nindex[src + 1] = i + 1;
      gout.nlist[i] = dst;
    }
       std::sort(v.begin(), v.end(), sortbysec);

    gin.nindex[0] = 0;
    for (int i = 0; i < edges; i++) {
      int src = std::get<0>(v[i]);
      int dst = std::get<1>(v[i]);
      gin.nindex[dst + 1] = i + 1;
      gin.nlist[i] = src;
    }
    for (int i = 0; i < gin.nodes; i++){
      for (int v = gin.nindex[i]; v < gin.nindex[i+1]; v++){
        int n = gin.nlist[v];
        printf("%d\t%d\n",i, n);
      }

    }
  }

  for (int i = 1; i < (nodes + 1); i++) {
    gout.nindex[i] = std::max(gout.nindex[i - 1], gout.nindex[i]);
  }

  for (int i = 1; i < (nodes + 1); i++) {
    gin.nindex[i] = std::max(gin.nindex[i - 1], gin.nindex[i]);
  }

  writeECLgraph(gin, argv[2]);
  writeECLgraph(gout, argv[3]);
  freeECLgraph(gin);
  freeECLgraph(gout);
  return 0;
}
