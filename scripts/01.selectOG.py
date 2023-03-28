import sys 
from Bio import SeqIO
import os
from pprint import pprint

foresp = open(sys.argv[1],'r') # 前景之物种名文件
fornum = int(sys.argv[2]) # 应该包含的物种个数
bkgesp = open(sys.argv[3],'r') # 背景物种名文件
bkgnum = int(sys.argv[4]) # 应该包含的物种个数
orthogroup = open(sys.argv[5],'r') # orthogroup.txt "cat Orthogroups.txt | tr " " ";" > Orthogroups.txt.tmp"
cds_file = open(sys.argv[6],'r') # cds all file  "cat *"
pep_file = open(sys.argv[7],'r') # pep all file  "cat *"

def read_sp (filename,outlst):
    for line in filename :
        line = line.strip()
        outlst.append(line)
    return outlst

def stat_count (spec_lst,spec_num,allinfo,stat):
    com = [val for val in spec_lst if val in allinfo ]
    num = len(com)
    if num >= spec_num :
        stat.append("1")
    else :
        stat.append("2") 
    return stat

forlst = []
bkglst = []
OG_filter = {}

read_sp(foresp,forlst)
read_sp(bkgesp,bkglst)

for line in orthogroup :
    line = line.strip().split(";")
    OGname = line[0].replace(":","")
    info = line[1:]
    ex_info = []
    for a in info :
        jkl = a.split("|")[0]
        if jkl not in ex_info :
            ex_info.append(jkl)
    stat1 = []
    stat2 = []
    stat_count(forlst,fornum,ex_info,stat1)
    stat_count(bkglst,bkgnum,ex_info,stat2)
    if "1" in stat1 and "1" in stat2:
        OG_filter[OGname] = info

if not os.path.exists("filter"):
    os.makedirs("filter")

cds_dic = SeqIO.to_dict(SeqIO.parse(cds_file, "fasta"))
pep_dic = SeqIO.to_dict(SeqIO.parse(pep_file, "fasta"))

for i in OG_filter :
    ogname = i 
    info = OG_filter[i]
    #pprint(info)
    pat = "filter/" + ogname
    os.makedirs(pat)
    cds_outputfile = pat + "/cds"
    pep_outputfile = pat + "/pep"
    with open(cds_outputfile,'a+') as cds_out , open(pep_outputfile,'a+') as pep_out :
        for a in info :
            cds_out.write(">"+a+"\n"+str(cds_dic[a].seq)+"\n")
            pep_out.write(">"+a+"\n"+str(pep_dic[a].seq)+"\n")

foresp.close()
bkgesp.close()
orthogroup.close()
