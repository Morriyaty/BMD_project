treefile=$1
forlist=$2

cat $treefile | sed 's/:[0-9.]\+//g' > temp.tree

cat $forlist | while read a 
do
	sed -i "s/\(${a}|[A-Za-z0-9_.]\+\)\([,()]\)/\1{test}\2/g" temp.tree
done

mv temp.tree hyphy.input.tree
