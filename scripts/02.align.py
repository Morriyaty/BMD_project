import glob

files = glob.glob("filter/*")

for i in files :
    print("mafft --auto " + i + "/pep > " + i + "/pep.best.fas && pal2nal.pl " + i + "/pep.best.fas " + i + "/cds -output fasta > " + i + "/cds.best.fas")
