# BMD_project
some scripts used for BMD

updating.....

#### software dependence
1. seqtk (insatll by conda)
2. iTools (https://github.com/BGI-shenzhen/Reseqtools)
3. mafft
4. pal2nal.pl
5. parallel
6. trimal (insatll by conda)
#### perl packages
1. Bio::SeqIO

#### python packages
1. Biopython
2. re

## compare genome analysis

### positive selection via orthogroup genes by hyphy
####1. filter gff file  

`sed -i -e 's/gene-//g' -e 's/rna-//g' -e 's/cds-//g' test.gff`

####2. get orthofindr input pep files 

`sh get_orthofinder_input.sh -g test.fa -a test.gff -s test  -t ~/software/iTools_Code/ -c ../scripts/`

####3. select ortholog genes of interests and get their pep and cds

```
cat OrthoFinder/Results_Mar28/Orthogroups/Orthogroups.txt | tr " " ";"  > Orthogroups.txt.tmp 

python3 01.selectOG.py forest.list 4 bkgest.list 7 Orthogroups.txt.tmp all.cds.clean.fa all.pep.clean.fa
```

note:  forest.list shows species name you interest in,

   bkgest.list shows species name of background,
       
   4 and 7 mean the species number should exit in one ortholog,
        
   fa: cat all fasta in one file

   when you have done this, a dic named "filter" wile exits under the folder

####4. get cds align files

```
python3 02.align.py > 02.align.py.sh

parallel -j 50 < 02.align.py.sh
```

####5. select only one sequence in one specie (min gap number)

```
python3 02.5.longestSeq.py
```

####6. filter gap in cds align files 

```
python3 03.trimal.py > 03.trimal.py.sh

parallel -j 50 < 03.trimal.py.sh

rm filter/*/*.fas  remove extra files 
```

####7. get ortholog gene tree based on iqtree

```
python3 04.iqtree.py > 04.iqtree.py.sh

parallel -j 50 < 04.iqtree.py.sh
```

####8. trans tree-file into hyphy input format

```
python3 05.newformatTREE.py > 05.newformatTREE.py.sh

parallel -j 50 < 05.newformatTREE.py.sh
```

####9. run hyphy absrel model

```
python3 06.hyphyrun.py > 06.hyphyrun.py.sh

parallel -j 50 < 06.hyphyrun.py
```

####10. stat hyphy output files 

```
python3 07.stat.py
```

####11. find forest.list all omega > 1 ortholog

```
python3 08-1.TESTMT1.py forest.list 6  > forest6.og.txt
```

note: if you want 5 or less species in forest.list, just change 6 to 5.

####12. find genes according to og name 

```
python3 09.findgenes.py Orthogroups.txt.tmp forest5.og.txt forest.list forest5.og.gene.txt
```

####13. align gene name in gff to gene symbol

```
cat forest5.og.gene.txt | cut -f 2 | sed 's/GS|//g' | sed 's/model/TU/' > forest5.og.gene.txt.tmp
python3 10.genealign.py forest5.og.gene.txt.tmp /opt/synData/anx21/BMD-work/01.Mus.hifi/02.minimap2/01.vcf.ano/gs.gene.align > zokor5.gene.list
```

note: format of gs.gene.align, you can get it from gff file

![微信截图_20230403101713](https://user-images.githubusercontent.com/68643810/229396669-73d796cb-5d0e-4d7f-bb34-9c0439371617.png)

####14. 
