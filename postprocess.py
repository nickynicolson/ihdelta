import sys
import pandas as pd
import numpy as np
import argparse

# Simple script to convert JSON to CSV

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    args = parser.parse_args()

    df = pd.read_json(args.inputfile)
    outputfile = args.inputfile.replace('.json','.csv')
    print('{} -> {}'.format(args.inputfile, outputfile))
    df.to_csv(outputfile, index=False, sep='\t')