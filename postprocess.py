import sys
import pandas as pd
import numpy as np
import argparse
import json

# Simple script to convert JSON to CSV

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    args = parser.parse_args()

    with open(args.inputfile, 'r') as f:
        ih_response = json.load(f)

    print(ih_response['meta'])
    df = pd.DataFrame(ih_response['data'])
    print(df)
    print(df.sample(n=1).T)

    outputfile = args.inputfile.replace('.json','.csv')
    print('{} -> {}'.format(args.inputfile, outputfile))
    df.to_csv(outputfile, index=False, sep=',')