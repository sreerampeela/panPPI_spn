import pandas as pd
import os
import get_edgetype as ge
randnets = [i.rstrip() for i in os.listdir() if i.endswith("_net.csv") is True]
# print(len(randnets))
fin = open("essential_proteins_list.txt",'r',newline="\n",encoding="utf-8")
essential_prots = [i.rstrip() for i in fin.readlines()]
df_edgetypes = pd.DataFrame(columns=["net_id", "E-E", "E-N", "N-E","N-N"])
ids = []
ee = []
en = []
ne = []
nn = []
for randnet in randnets:
  print(randnet)

  with open(randnet, 'r+') as file:
    if file.readline != "from to NA":
      readcontent = file.read()  # store the read value of exe.txt into 
                                # readcontent 
      file.seek(0, 0) #Takes the cursor to top line
    # for i in num:         # writing content of list One by One.
      file.write(" ".join(["from","to","NA"]) + "\n") #convert int to str since write() deals 
                                   # with str
      file.write(readcontent) 
  e_e,e_n,n_e,n_n = ge.getEdgetype(essential_prots, net=randnet)
  ids.append(randnet)
  ee.append(e_e)
  en.append(e_n)
  ne.append(n_e)
  nn.append(n_n)

df_edgetypes["net_id"] = ids
df_edgetypes["E-E"] = ee
df_edgetypes["E-N"] = en
df_edgetypes["N-E"] = ne
df_edgetypes["N-N"] = nn

print(df_edgetypes.head())

df_edgetypes.to_csv("edgetypes_rand.csv",header=True, index=False)