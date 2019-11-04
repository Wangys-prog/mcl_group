############ del_Brackets.py #############################
del_Brackets.py -h 
del_Brackets.py -i inputfile
Rapidly evolving families from cafe(CAFE: a computational tool for the study of gene family evolution):
The input file of rapidly evolving families was obtained by CAFE Report Analysis python script of Xu,gengzhou(https://www.jianshu.com/p/146093c91e2b)
    Input file format:
    Bg<22>:	OG0000018[+8*]	OG0000032[+57*]	OG0000035[+17*]	OG0000037[+4*]	OG0000065[-2*]	OG0000096[-2*]	OG0000215[-2*]	
    Um<4>:	OG0000308[+7*]	OG0000418[+5*]	OG0000024[-5*]	OG0000047[-3*]	OG0000050[-4*]	OG0000088[-3*]	OG0000104[-4*]	
    Vi<18>: OG0000001[+8*]	*]	OG0005047[+3*]	OG0005053[+2*]	008022[+3*]	OG0008156[+6*]	OG0008375[+3*]	OG0008565[+2*]	
    <33>:  OG0000000[+14*]	OG0000001[+5*]	OG0000002[+3*]	OG0000004[+4*]	OG0000008[+3*]
    <25>: OG0000018[+4*]	 OG0000032[+4*]	OG0000035[+4*]	OG0000012[-2*]	OG0000019[-2*]	OG0000021[-2*]	OG0000049[-2*]	OG0000053[-2*]	
################ mcl_group2.py ############################################
python mcl_group2.py -h

 Input file format(-i) : outfile from del_Brackets.py
     Bg<22>:	OG0000018	OG0000032	OG0000035	OG0000037	OG0000088	OG0000107	OG0000110	OG0000135	OG0000136	OG0000150	OG0000179	OG0000306	
     Um<4>:	OG0000308	OG0000418	OG0000726	OG0001108	OG0001256	OG0001395	OG0001847	OG0002971	OG0004707	OG0006752
    Vi<18>:	OG0000001	OG0000003	OG0000012	OG0000022	OG0000024	OG0000042	OG0000045	OG0000047	OG0000049	OG0000050	OG0000051	OG0000052	
    <33>:	OG0000000	OG0000001	OG0000002	OG0000004	OG0000008	OG0000009	OG0000011	OG0000012	OG0000013	OG0000014	OG0000019	OG0000025	
   <25>:	OG0000018	OG0000032	OG0000035
Input file format(-f): outfile from del_Brackets.py
   OG0000000
   OG0000001
   OG0000002
   OG0000003
   OG0000004
   OG0000005
   OG0000006

#################### mcl_group ############################
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
