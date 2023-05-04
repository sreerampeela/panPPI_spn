from multiprocessing import Pool
import networkx as nx
import random
import time
import pandas as pd
import numpy as np
import os
import itertools
# from matplotlib.pyplt import plt

# functions


def randomizeNetwork(G, rand_seed=100, no_swaps=0.2, graph_out="random_test.tab"):
    """To randomize a directed graph (edge list) by using Networkx Directed edge swap."""
    graph_in = nx.read_edgelist(G, create_using=nx.DiGraph)
    nx.double_edge_swap(graph_in.to_undirected(), nswap=graph_in.number_of_edges(
    )*no_swaps, max_tries=100000, seed=rand_seed)
    nx.write_edgelist(graph_in, graph_out, data=False, delimiter='\t')
    return graph_in


def chunks(l, n):
    """Divide a list of nodes `l` in `n` chunks"""
    l_c = iter(l)
    while 1:
        x = tuple(itertools.islice(l_c, n))
        if not x:
            return
        yield x


def betweenness_centrality_parallel(G, processes=None):
    """Parallel betweenness centrality  function"""
    p = Pool(processes=processes)
    node_divisor = len(p._pool) * 12
    node_chunks = list(chunks(G.nodes(), G.order() // node_divisor))
    num_chunks = len(node_chunks)
    bt_sc = p.starmap(
        nx.betweenness_centrality_subset,
        zip(
            [G] * num_chunks,
            node_chunks,
            [list(G)] * num_chunks,
            [True] * num_chunks,
            [None] * num_chunks,
        ),
    )

    # Reduce the partial solutions
    bt_c = bt_sc[0]
    for bt in bt_sc[1:]:
        for n in bt:
            bt_c[n] += bt[n]
    return bt_c


def node_mapping(filein):
    df = pd.read_csv(filein, sep='\t', header=0, encoding='unicode_escape')
    print(df.head())
    stringid = df["target"]
    geneid = df["gene_target"]

    mappings = dict()
    for i in range(len(stringid)):
        mappings[stringid[i]] = geneid[i]

    return mappings


def getEdgetype(original_net="ncbi_3_blast.tab", small_net="spn_largecc_edgelist.tab", blast_results="spn_proteome_blast.csv"):
    df = pd.read_csv(small_net, sep="\t")
    df.columns = ["source", "target"]
    df2 = pd.read_csv(original_net, sep='\t', encoding='unicode_escape')
    sources = [i.rstrip() for i in df["source"]]
    targets = [i.rstrip() for i in df["target"]]
    stringid = [i.rstrip() for i in df2["source"]]
    geneid = [i.rstrip() for i in df2["gene_source"]]

    stringtogene_dict = dict()
    
    for i in range(len(stringid)):
        stringtogene_dict[stringid[i]] = geneid[i]
        

    blast_res = open(blast_results, 'r', newline='\n', encoding='utf-8')

    essential_pan = []
    for i in list(blast_res.readlines()):
        if i.split(",")[6] == "yes" and i.split(",")[8] == "yes" and i.split(",")[10] == "yes":
            essential_pan.append(stringtogene_dict[i.split(",")[0]])

    blast_res.close()
    source_essential = []
    target_essential = []
    for j in sources:
        if j in essential_pan:
            source_essential.append("y")
        else:
            source_essential.append("n")

    for k in targets:
        if k in essential_pan:
            target_essential.append("y")
        else:
            target_essential.append("n")

    df["source_essential"] = source_essential
    df["target_essential"] = target_essential

    edge_type = []
    for i in range(len(source_essential)):
        if source_essential[i] == "n" and target_essential[i] == "n":
            edge_type.append("N-N")
        elif source_essential[i] == "n" and target_essential[i] == "y":
            edge_type.append("N-E")
        elif source_essential[i] == "y" and target_essential[i] == "n":
            edge_type.append("E-N")
        elif source_essential[i] == "y" and target_essential[i] == "y":
            edge_type.append("E-E")

    df["edge_type"] = edge_type
    
    return df
    



