import pandas as pd
import optparse
import sys

parser = optparse.OptionParser()

parser.add_option('-a', '--EnTAPannotFile',
                  help="input file name (.tsv)",
                  default=False,
                  )

parser.add_option('-t', '--entapTransColName',
                  help="Column header name of trinity transcript ids EnTAP Annotation File",
                  default=False,
                  )

parser.add_option('-d', '--deResultFile',
                  help="Differential Expression analysis output file (.tsv)",
                  default=False,
                  )

parser.add_option('-g', '--trinityGeneColName',
                  help="Column header name of trinity gene ids in deResultFile",
                  default=False,
                  )

parser.add_option('-o', '--outfile',
                  help="output file name (.csv)",
                  default="DESeq_Filtered.csv",
                  )

options,args = parser.parse_args()
option_dict = vars(options)

entap_file = option_dict.get('EnTAPannotFile')
outf = option_dict.get('outfile')
deres_file = option_dict.get('deResultFile')
deres_gene_col_name=option_dict.get('trinityGeneColName')
entap_trans_col_name=option_dict.get('entapTransColName')

# reading csv file from url 
entap_trans_df = pd.read_table(entap_file, sep='\t+', engine='python')
deresult_df=pd.read_table(deres_file, sep='\t+', engine='python')
   
# dropping null value columns to avoid errors
#data.dropna(inplace = True)
   
# new data frame with split value columns
#entap_trans_df["Trinity_GENE"]= entap_trans_df["Trinity_Transcript"].str.split("_c", n = 1, expand = True)

#entap_trans_df[['Trinity_Transcript']] = entap_trans_df["Trinity_Transcript"].apply(lambda x: pd.Series(str(x).split("_c")))

entap_trans_df[[deres_gene_col_name,'purge']] = entap_trans_df[entap_trans_col_name].str.split("_c",expand=True)
entap_trans_df.pop("purge")# df display
#print(entap_trans_df)

merged_df=pd.merge(deresult_df,entap_trans_df,on=deres_gene_col_name,how='left')

merged_df.to_csv(outf, index=False)

