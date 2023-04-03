import sys 

f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'r')

x = []

for line in f1:
    line = line.strip()
    x.append(line)

for line in f2 :
    line = line.strip().split("\t")
    if line[0].replace("ID=","") in x :
        if len(line) >= 1 :
            print(line[1].split("=")[1])
        else :
            print("Unknow")

f1.close()
f2.close()
