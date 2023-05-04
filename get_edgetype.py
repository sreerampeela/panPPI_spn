import os
import networkx as nx
import pandas as pd

def getEssential(blast_res="spn_proteome_renamed_blast_new.csv"):
    blast_results = pd.read_csv(blast_res, header=0)
    essential_pan = []
    prots = list(set(blast_results["qseqid"]))
    for i in range(len(prots)):
        source = prots[i]
        blast_out = blast_results.loc[blast_results["qseqid"] == source]
        if len(blast_out.index) != 0:
            qlen = int(blast_out["qlen"])
            sublen = int(blast_out["slen"])
            align_len = int(blast_out["length"])
            identity = int(blast_out["pident"])
            evalue = int(blast_out["evalue"])
            qcov = align_len/qlen * 100
            scov = align_len/sublen * 100
            if (qcov >= 95) and (scov >= 95) and (identity >= 95) and (evalue <= 0.05):
            # print(source)
                essential_pan.append(source)
    return essential_pan

def getEdgetype(essential_prots, net="rand_igraph_1_net.csv"):
    small_net = pd.read_csv(net,delimiter=",",header=0)
    # print(small_net.head(30))
    withedgetype = "withedgetype_" + net
    sources = [i for i in small_net["from"]]
    targets = [i for i in small_net["to"]]
    source_essential = []
    target_essential = []
    for j in sources:
        if j in essential_prots:
            source_essential.append("y")
        else:
            source_essential.append("n")

    for k in targets:
        if k in essential_prots:
            target_essential.append("y")
        else:
            target_essential.append("n")

    small_net["source_essential"] = source_essential
    small_net["target_essential"] = target_essential
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
    small_net["edge_type"] = edge_type
    e_e = edge_type.count("E-E")
    n_e = edge_type.count("N-E")
    e_n = edge_type.count("E-N")
    n_n = edge_type.count("N-N")
    small_net.to_csv(withedgetype, index=False,header=True)
    return e_e,e_n,n_e,n_n

ess = getEssential()

e_e,e_n,n_e,n_n = getEdgetype(ess,net="undirected_original_edgelist.csv")

print(e_e,e_n,n_e,n_n)
