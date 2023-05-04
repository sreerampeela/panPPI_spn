import networkx as nx
import pandas as pd
import randomise_net as rn
import time

df = pd.read_csv("undirected_original_edgelist.csv", header = 0)
g1 = nx.from_pandas_edgelist(df, source = "from", target = "to", create_using=nx.Graph)
# print(g1.nodes())
# print(g1.number_of_edges())
# print(nx.clustering(g1))
genes = list(g1.nodes(data=False))
header = ["net_id"]
for g in genes:
    header.append(g)
df_calc = pd.DataFrame(columns=[header])
df_calc.fillna(0)
print(df.shape)

# start analysis of rand networks
start = time.time()

for i in range(1000):
    net_name = "rand_0.1_" + str(i) + "_net.csv"
    rand_net = nx.double_edge_swap(g1,nswap = int(g1.number_of_edges() * 0.1), max_tries = 10000, seed = 1987)
    # df_net = pd.read_csv(net_name,sep=' ')
    # df_net.columns = ["from","to","data"]
    # rand_net = nx.from_pandas_edgelist(df_net, source = "from", target = "to", create_using=nx.Graph)
    btn = rn.betweenness_centrality_parallel(rand_net)
    print(i)
    mes = [net_name]
    for gene in list(btn.keys()):
        cent = btn[gene]
        mes.append(cent)
    df_calc.loc[i] = mes
    nx.write_edgelist(rand_net,net_name)

df_calc.to_csv("rand_0.1_btnness.csv")


print(f"\t\tTime: {(time.time() - start):.3F} seconds")