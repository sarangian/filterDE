FilterDE
========
    filter GEGs from DESeq2 or EDGR analysis based on log2fc and pvalue 
    dependancies: optparse

    ./FilterDE.py -h
    Usage: FilterDE [options]

Options
=======
    -h, --help            show this help message and exit
    -i INFILE, --infile=INFILE
                        input file name (.tsv)
    -o OUTFILE, --outfile=OUTFILE
                        output file name (.csv)
    -p PVALCOLNAME, --pvalcolname=PVALCOLNAME
                        Please enter the column header name that contains
                        P-Values
    -l LOGFCCOLNAME, --logFCcolname=LOGFCCOLNAME
                        Please enter the column header name that contains
                        Log2FC values
    -f FOLDCHANGE, --foldchange=FOLDCHANGE
                        cut-off for log2 fold change value
