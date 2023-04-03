import sys 
import glob

f1 = open(sys.argv[1],'r')
f2 = int(sys.argv[2])

x = []

for line in f1 :
    line = line.strip()
    x.append(line)

files = glob.glob("filter/*/hyphy.output.txt")


for i in files :
    ortholog = i.split("/")[1]
    with open(i,'r') as infile :
        a = 0
        for line in infile :
            line = line.strip().split()
            if line[0][:2] in x and float(line[1]) >= 1 :
                a = a + 1 
        if a >= f2 :
            print(ortholog+"\t"+str(a))

f1.close()
