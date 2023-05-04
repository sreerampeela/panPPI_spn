import pandas as pd
import numpy as np
from scipy import stats as st

# fout = open("essential_bc_stats.txt",'a',newline="\n",encoding="utf-8")
# fout.write("\t".join(["gene","observed","random_nets","t-statistic","pvalue"])+"\n")
fin = open("essential_proteins_list.txt","r", encoding="utf-8",newline="\n")
essential_proteins = [i.rstrip() for i in fin.readlines()]

p_no = "SPD_1959,tkt,clgD,SP_0917,dapH,talC,dgkA,spr0587,SPD_1128,SPD_1850," \
    "SP_1173,pfkA,deoD,ccdA-2,SPD_0588,SPD_1944,lepA,SPD_1648,SPD_1265,SP_1329," \
    "serS,SPD_0712,SPD_1536,SPD_1199,dnaN,SPD_1177,SPD_1803,SPD_0229,thrS," \
    "SPD_0727,SPD_1467,ung,pyrG,malQ,pstS,SPD_1830,SPD_1783,SP_0926,nikS".split(",")

print(len(p_no))

p_no_ess = []

for i in p_no:
    if i in essential_proteins:
        p_no_ess.append(i)

print(p_no_ess)

# dframe = pd.read_csv("original_net_analysis.csv",header = [0])
# essential_btwnness = dict()
# # nonessential_btwnness = []
# node_names = list(dframe["name"])

# for prot in node_names:
#     # print(prot)
#     b = dframe.loc[dframe["name"]==prot,"BetweennessCentrality"]
#     b_value = b.values[0]
#     if prot in essential_proteins:
#         # print(b_value)
#         essential_btwnness[prot] = b_value
#     # else:
#     #     nonessential_btwnness.append(b_value)


# # essential_mean = np.array(essential_btwnness).mean()
# df3 = pd.DataFrame(columns=["gene","observed","random_nets","t-statistic","pvalue"])
# gene_names = []
# observed_btn = []
# rand_mean = []
# t_stat = []
# pvals = []
# df2 = pd.read_csv("rand_0.1_btnness.csv", header=0)
# for gene in essential_btwnness:
#     rand_btness = df2[gene]
#     # mean_rand_btnness = rand_btness.mean()
#     observed = essential_btwnness[gene]
#     t_test = st.ttest_1samp(a=rand_btness, popmean=observed)
#     gene_names.append(gene)
#     observed_btn.append(observed)
#     rand_mean.append(rand_btness.mean())
#     t_stat.append(t_test.statistic)
#     pvals.append(t_test.pvalue)

# df3["gene"] = gene_names
# df3["observed"] = observed_btn
# df3["random_nets"] = rand_mean
# df3["t-statistic"] = t_stat
# df3["pvalue"] = pvals

# print(df3.head(10))

# df3.to_csv("essential_nodes_btnness.csv",header=True,index=False)
