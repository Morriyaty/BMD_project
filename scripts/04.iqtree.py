import glob

files = glob.glob("filter/*")

for i in files :
    print("iqtree -s " + i + "/cds.best.fas.fltgap.fa && cd " + i + " && rm *.gz *log *mldist *iqtree & cd ../..")
