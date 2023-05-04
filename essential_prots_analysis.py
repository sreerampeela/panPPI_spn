import pandas as pd
import numpy as np
from scipy import stats as st
# import matplotlib.pyplot as plt
import random
fout = open("essential_stats.txt",'a',newline="\n",encoding="utf-8")
fout.write("\t".join(["iter","t-statistic","pvalue"])+"\n")
fin = open("essential_proteins_list.txt","r", encoding="utf-8",newline="\n")
essential_proteins = [i.rstrip() for i in fin.readlines()]

dframe = pd.read_csv("original_net_analysis.csv",header = [0])
essential_btwnness = []
nonessential_btwnness = []
node_names = list(dframe["name"])

for prot in node_names:
    # print(prot)
    b = dframe.loc[dframe["name"]==prot,"BetweennessCentrality"]
    b_value = b.values[0]
    if prot in essential_proteins:
        # print(b_value)
        essential_btwnness.append(b_value)
    else:
        nonessential_btwnness.append(b_value)


essential_mean = np.array(essential_btwnness).mean()
nonessential_mean = np.array(nonessential_btwnness).mean()


for i in range(10000):
    random_data = random.sample(nonessential_btwnness,len(essential_btwnness))
    random_mean = np.array(nonessential_btwnness).mean()
    t_test = st.ttest_ind(essential_btwnness,random_data, alternative='two-sided')
    print(t_test)
    data = "\t".join([str(i),str(t_test.statistic),str(round(t_test.pvalue,6))])
    fout.write(data+"\n")


fin.close()
fout.close()
