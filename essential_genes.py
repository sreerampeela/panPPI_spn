import os
import pandas as pd
import numpy as np
import get_edgetype as ge
from scipy import stats as st

# rand_nets = [i for i in os.listdir() if i.endswith("_net.csv") is True]
fout = open("btnness_random_stats.txt",'a',newline="\n",encoding="utf-8")
fout.write("\t".join(["gene","original_net","random_net","t-statistic","pvalue"])+"\n")
df_edgetypes = pd.DataFrame(columns=["net_id", "E-E", "E-N", "N-E","N-N"])
original_net = pd.read_csv("undirected_original_edgelist.csv", header=[0])
source_ids = original_net["from"]
target_ids = original_net["to"]
ess_genes = ge.getEssential()
e_e,e_n,n_e,n_n = ge.getEdgetype(ess_genes,net="undirected_original_edgelist.csv")
print(e_e,e_n,n_e,n_n)
edge_types = [e_e,e_n,n_e,n_n]
genes = list(set(list(source_ids)+ list(target_ids)))
# ids = []
# ee = []
# en = []
# ne = []
# nn = []
# ess = ge.getEssential()
# for i in rand_nets:
#   print(i)
#   e_e,e_n,n_e,n_n = ge.getEdgetype(ess, net=i)
#   ids.append(i)
#   ee.append(e_e)
#   en.append(e_n)
#   ne.append(n_e)
#   nn.append(n_n)

# df_edgetypes["net_id"] = ids
# df_edgetypes["E-E"] = ee
# df_edgetypes["E-N"] = en
# df_edgetypes["N-E"] = ne
# df_edgetypes["N-N"] = nn

# print(df_edgetypes.head())

# df_edgetypes.to_csv("edgetypes_rand.csv",header=True, index=False)

df2 = pd.read_csv("rand_0.1_btnness.csv",header=[0])
dframe = pd.read_csv("original_net_analysis.csv",header = [0])
for gene in genes:
    rand_btness = np.array(df2[gene])
    rand_mean = np.mean(rand_btness)
    # rand_mean = 
    pop_cc = dframe.loc[dframe["name"]==gene,"BetweennessCentrality"].values[0]
    t_test = st.ttest_1samp(a=rand_btness, popmean=pop_cc)
    d = "\t".join([gene,str(pop_cc),str(rand_mean),str(t_test.statistic),str(t_test.pvalue)])
    fout.write(d+"\n")
    

fout.close()








