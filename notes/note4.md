# biological interpretation

from the huge data analysis that we performed we were able to identify some interesting sites in the genome of the phages that were targeted by selective pressure.

Thanks to the genome annotation of these phages we can which are the affected genes:

## summary

| Phage  | type of divergence | position | gene                                                                |
| ------ | ------------------ | -------- | ------------------------------------------------------------------- |
| EM11   | snp                | 36588    | lateral tail fiber protein with glycosidase and deacetylase domains |
| EM11   | snp                | 30397    | lateral tail fiber protein with fibronectin type III domain         |
| EM11   | snp                | 7328     | major capsid protein                                                |
| EM60   | snp                | 36619    | lateral tail fiber protein with glycosidase and deacetylase domains |
| EM60   | snp                | 7695     | major capsid protein                                                |
| EM11   | gap                | 43327    | lateral tail fiber protein with intimin domain                      |
| EM60   | gap                | 28977    | lateral tail fiber protein with fibronectin type III domain         |
| EM60   | gap                | 44969    | lateral tail fiber protein with intimin domain                      |

## EM11

EM11 showed few interesting mutations, two of them follow more or less the same pattern along the days and they affect genes with similar function.

These mutations affect genes involved in the lateral tail fiber protein.



2. the site of EM60 that you found (36619) corresponds to 79121 in my assembly and i discarded it because the coverage was less than 50 and the difference between forward and reverse frequency is 0.33 at timepoint 1. I corrected the thresholds and now i have it in the plot.

3. the sites with non consensus frequency of 0.4 that I found in EM60 map at 7695 and 7696 in the reference genome. they are part of the major capisd protein, they are the first two positions of the last codon of the gene.

4. the sites with gap frequency at 0.3 that I found in EM60 map at 28977 and 44969 in the reference genome. they are part of lateral tail fiber proteins

5. I tried to put a low threshold on the score of the first timepoint but nothing fancy happened

6. I noticed that in the non consensus frequency graph of EM11 there is a site that follows a similar path as the two i found in EM60 (reaching .3 of non consensus frequency). it maps at 7328 on the reference, part of major capsid protein gene.

## entropy

score on the basis of an entropy, if there is less disorder we give more power to the observation


## aminoacid mutaitons 
look at aminoacid changes in all mutations 

EM11 82280 aspartate(GAC) to glycine(GGC)

## secondary mapping

2bef93e1-3ad8-4eb7-b28d-5cba95221d27
98222.5
88534.0
f4d3a673-f458-4f7e-bd43-d6c540bb10db
98595.0
88704.5
9fcd9145-95f8-4fe7-ad1d-1a649bd62bc0
98419.0
88844.0
2b770158-c5ea-4487-9bcf-dc63deed197b
97651.0
88861.5
1ad37322-6291-4880-8a58-71bdf2fe3612
97210.0
89085.0
7f5b8127-6bcf-4b33-8b78-28a1347ffb9f
97763.0
88929.5
b1c60e02-5fd6-49ce-9d64-1a35d7116459
96297.0
89195.5

![Alt text](image.png)

## 3d structure

mutated
![Alt text](image-1.png)


non mutated
![Alt text](image-2.png)










red line in fastq quality

are methylation sites increasing?

36619 reference site with high ncf, corresponds to 79121 in my assembly
this ite has coverage <100 and divergence between forward and reverse at timepoint 1 is 0.33