import glob

files = glob.glob("filter/*")

for i in files :
    print("hyphy absrel --alignment " + i + "/cds.best.fas.fltgap.fa --tree " + i + "/hyphy.input.tree --output " + i + "/hyphy.output  CPU=10")
