import pandas as pd

def do(x):
    x = str(x)
    x = x.split(';')
    if len(x) == 1 and x[0] == 'nan':
        return 0
    else:
        return len(x)

kdf = pd.read_excel('KCategorizedDataLysC2.xlsx')
# rdf = pd.read_excel('RCategorizedDataTrypsin2.xlsx')

kdf1 = pd.DataFrame()
# rdf1 = pd.DataFrame()

kdf['frequency'] = kdf['Peptides'].apply(do)
# rdf['frequency'] = rdf['Peptides'].apply(do)

# Copying data to 'Neg' columns from row 0 onwardsastype(str)
kdf1['Category'] = kdf['Category'].iloc[:110].copy()
kdf1['Peptides'] = kdf['Peptides'].iloc[:110].copy()
kdf1['frequency'] = kdf['frequency'].iloc[:110].copy()
kdf1['Neg Category'] = kdf['Category'].iloc[110:].copy().reset_index(drop=True)
kdf1['Neg Peptides'] = kdf['Peptides'].iloc[110:].copy().reset_index(drop=True)
kdf1['Neg frequency'] = kdf['frequency'].iloc[110:].copy().reset_index(drop=True)

# rdf1['Category'] = rdf['Category'].iloc[:110].copy()
# rdf1['Peptides'] = rdf['Peptides'].iloc[:110].copy()
# rdf1['frequency'] = rdf['frequency'].iloc[:110].copy()
# rdf1['Neg Category'] = rdf['Category'].iloc[110:].copy().reset_index(drop=True)
# rdf1['Neg Peptides'] = rdf['Peptides'].iloc[110:].copy().reset_index(drop=True)
# rdf1['Neg frequency'] = rdf['frequency'].iloc[110:].copy().reset_index(drop=True)

kdf1.to_excel('KFreqDataLysC2.xlsx', index=False)
# rdf1.to_excel('RFreqDataTrypsin2.xlsx', index=False)
