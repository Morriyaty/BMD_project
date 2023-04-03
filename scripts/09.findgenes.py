import sys 

f1 = open(sys.argv[1],'r') # ortholog
f2 = open(sys.argv[2],'r') # 08.output
f3 = open(sys.argv[3],'r') # forest
f4 = open(sys.argv[4],'w') # this output

sp = []
og = []

for line in f2 :
    line = line.strip().split()
    og.append(line[0])

for line in f3 :
    line = line.strip()
    sp.append(line)

for line in f1 :
    line = line.strip().split(";")
    info = line[1:]
    if line[0].replace(":","") in og :
        f4.write(line[0].replace(":","")+"\t")
        for i in info :
            name = i.split("|")[0]
            if name in sp :
                f4.write(i+"\t")
        f4.write("\n")

f1.close()
f2.close()
f3.close()
f4.close()
