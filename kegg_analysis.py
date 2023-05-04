from Bio.KEGG import REST
import requests as re
# from Bio.KEGG import Entry

# request = REST.kegg_get("SPD_1959")
# print(request.read().decode("utf-8"))

url = "https://rest.kegg.jp/find/"

params = {
    db : "genes",
    query : "tkt"
    org : "spn"

}

# request = re.