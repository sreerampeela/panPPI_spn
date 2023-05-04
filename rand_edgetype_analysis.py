import pandas as pd
from scipy import stats as st

e_e,e_n,n_e,n_n = 1000, 1157, 1402, 5495

df = pd.read_csv("edgetypes_rand.csv", header=0)

eeEdges = df["E-E"]
neEdges = df["N-E"]
enEdges = df["E-N"]
nnEdges = df["N-N"]

ee_t_test = st.ttest_1samp(a=eeEdges,popmean=e_e)
ne_t_test = st.ttest_1samp(a=neEdges,popmean=n_e)
en_t_test = st.ttest_1samp(a=enEdges,popmean=e_n)
nn_t_test = st.ttest_1samp(a=nnEdges,popmean=n_n)
print(ee_t_test.pvalue)
print(ne_t_test)
print(en_t_test)
print(nn_t_test)
# print([type(i) for i in eeEdges])

dfres = pd.DataFrame(columns=["edgetype","observed","randomnets_mean","t_statistic","pvalue"])
dfres["edgetype"] = ["E-E","N-E","E-N","N-N"]
dfres["observed"] = [1000,1402,1157,5495]
dfres["randomnets_mean"] = [eeEdges.mean(),neEdges.mean(),enEdges.mean(),nnEdges.mean()]
dfres["t_statistic"] = [ee_t_test.statistic,ne_t_test.statistic,en_t_test.statistic,nn_t_test.statistic]
dfres["pvalue"] = [ee_t_test.pvalue,ne_t_test.pvalue,en_t_test.pvalue,nn_t_test.pvalue]
print(dfres.head())

dfres.to_csv("edgetype_statistics.csv",header=True,index=False)