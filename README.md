# BMD_project
some scripts used for BMD

updating.....

#### software dependence
1. seqtk (insatll by conda)
2. iTools (https://github.com/BGI-shenzhen/Reseqtools)
3. mafft
4. pal2nal.pl
5. parallel
#### perl packages
1. Bio::SeqIO

## compare genome analysis

### step 1 get ortholog genes from orthofinder
####1. filter gff file  

`sed -i -e 's/gene-//g' -e 's/rna-//g' -e 's/cds-//g' test.gff`

####2. get orthofindr input pep files 

`sh get_orthofinder_input.sh -g test.fa -a test.gff -s test  -t ~/software/iTools_Code/ -c ../scripts/`

####3. select ortholog genes of interests and get their pep and cds

`cat OrthoFinder/Results_Mar28/Orthogroups/Orthogroups.txt | tr " " ";"  > Orthogroups.txt.tmp `

`python3 01.selectOG.py forest.list 4 bkgest.list 7 Orthogroups.txt.tmp all.cds.clean.fa all.pep.clean.fa`

note:  forest.list shows species name you interest in,

bkgest.list shows species name of background,
       
4 and 7 mean the species number should exit in one ortholog,
        
fa: cat all fasta in one file

when you have done this, a dic named "filter" wile exits under the folder

####4. get cds align files

`python3 02.align.py > 02.align.py.sh`

`parallel -j 50 < 02.align.py.sh`
