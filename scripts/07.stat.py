import sys 
import glob 
import re

files = glob.glob("filter/*/hyphy.output")

for i in files :
    output = i.replace("hyphy.output","hyphy.output.txt")
    with open(i,'r') as infile , open(output,'w') as outfile :
        for line in infile :
            line = line.strip()
            if ("_" in line and "{" in line and '(' not in line) or ("Node" in line and "{" in line and '(' not in line):
                name = re.search(r'\w+',line).group(0)
                outfile.write(name+"\t")
            elif "omega ratio" in line :
                value = re.sub(r'\s+','',line).split(":")[1].replace(",","")
                outfile.write(value+"\t")
            elif "Corrected" in line :
                p = re.sub(r'\s+','',line).split(":")[1].replace(",","")
                outfile.write(p+"\n")
            else :
                continue


