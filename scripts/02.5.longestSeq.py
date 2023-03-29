from Bio import SeqIO
import glob
from pprint import pprint
import re

files = glob.glob("filter/OG*")

for i in files :
    outputfile = i + "/cds.best.fas.filter.fa"
    x = {}
    cds_file = i + "/cds.best.fas"
    cds_dic = SeqIO.to_dict(SeqIO.parse(cds_file, "fasta"))
    for a in cds_dic :
        sp_name = a.split("|")[0]
        seq_name = a.split("|")[1]
        seq = str(cds_dic[a].seq)
        gap = len(re.findall(r'-',seq))
        if sp_name not in x :
            p = {}
            l1 = []
            l2 = []
            l3 = []
            l1.append(seq_name)
            l2.append(gap)
            l3.append(seq)
            p["name"] = l1
            p["length"] = l2
            p["sequence"] = l3
            x[sp_name] = p
        else :
            x[sp_name]["name"].append(seq_name)
            x[sp_name]["length"].append(gap)
            x[sp_name]["sequence"].append(seq)
    with open(outputfile,'w') as jkl:
        for j in x :
            name_l = x[j]["name"]
            gap_l = x[j]["length"]
            seq_l = x[j]["sequence"]
            locat = gap_l.index(min(gap_l))
            jkl.write(">"+j+"|"+name_l[locat]+"\n")
            jkl.write(seq_l[locat]+"\n")


