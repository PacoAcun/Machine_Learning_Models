import pandas as pd

def view_info(df):
    for c in df.columns[0:-1]:
        print(c)
        print(df[c].mean())
        print()
    return None