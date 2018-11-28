import pandas as pd
import sys
import os

def convert_to_csv(file):
    df = pd.read_html(file)

    df = df[0]

    df = df.iloc[6:-1,1:-1]

    info1 = df.iloc[1,1]
    info2 = df.iloc[2,1]

    df.insert(loc=len(df.columns), column='info1', value=info1)
    df.insert(loc=len(df.columns), column='info2', value=info2)
    df.columns = ['date', 'connect', 'num', 'service', 'measure', 'time', 'tariff', 'sum', 'info1', 'info2']
    df.to_csv(file.split('.')[0]+'.csv', sep=';', encoding='utf-8', index=False)

if __name__ == '__main__':
    path = sys.argv[1]
    files = os.listdir(path)
    files = [file for file in files if os.path.isfile(file) and '.xls' in file] # only .xls files
    
    for f in files:
        convert_to_csv(f)

    sys.exit()  