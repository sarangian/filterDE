#pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org optparse-pretty
import pandas as pd
import optparse
import sys

parser = optparse.OptionParser()

parser.add_option('-i', '--infile',
                  help="input file name (.tsv)",
                  default=False,
                  )

parser.add_option('-o', '--outfile',
                  help="output file name (.csv)",
                  default="DESeq_Filtered.csv",
                  )

parser.add_option("-p","--pvalcolname",
                  help = "Please enter the column header name that contains P-Values")

parser.add_option("-l","--logFCcolname",
                  help = "Please enter the column header name that contains Log2FC values")

parser.add_option('-f', '--foldchange',
                  help="cut-off for log2 fold change value",
                  default=2.0,
                  type="float",
                  )


options,args = parser.parse_args()
option_dict = vars(options)

inf = option_dict.get('infile')
outf = option_dict.get('outfile')
out_up="up_"+outf
out_down="down_"+outf
upfc = option_dict.get('foldchange')
downfc = -upfc

pcol=option_dict.get('pvalcolname')
lcol=option_dict.get('logFCcolname')

print ('input file  :', inf)
print ('output file :',  outf)
print ('out up file :',  out_up)
print ('out down file :',  out_down)
print ('log fold change cut-off :','[',upfc, '  ', downfc,']')


data = pd.read_table(inf, sep='\t+', engine='python')
sig_p = data[data[pcol] <=0.05]
result = sig_p[(sig_p[lcol] >= upfc) | (sig_p[lcol] <= downfc)]

filtered_genes = result.shape[0]
up_regulated=sig_p[(sig_p[lcol] >= upfc)]
up_regulated_gene_count=up_regulated.shape[0]

down_regulated=sig_p[(sig_p[lcol] <= downfc)]
down_regulated_gene_count=down_regulated.shape[0]

print ('Total number of genes filtered: ', filtered_genes)
print ('Up Regulated: ', up_regulated_gene_count)
print ('Down Regulated: ', down_regulated_gene_count)

result.to_csv(outf, index=False)
up_regulated.to_csv(out_up, index=False)
down_regulated.to_csv(out_down, index=False)
