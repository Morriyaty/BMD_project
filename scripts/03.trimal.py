import glob

files = glob.glob("filter/*")

for i in files :
    print("trimal -in " + i + "/cds.best.fas.filter.fa -out " + i + "/cds.best.fas.fltgap.fa -gappyout")
