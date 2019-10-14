# mcl_group
# mcl_group
#help
python mcl_group.py -h

(1) inputfile: group.txt from orthmcl

group1: a b c d 
group2: e f g h 
group3: i j k l 


(2) inputfile: sample_id.txt 
a
b
c
d
e
f
g
i
j
k
l

(3) outputfile: orthomcl_table.txt
sample a b c d e f g h i j k l 
group1 1 1 1 1 0 0 0 0 0 0 0 0
group2 0 0 0 0 1 1 1 1 0 0 0 0
group3 0 0 0 0 0 0 0 0 1 1 1 1
