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

### step 1 get ortholog genes from orthofinder
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
