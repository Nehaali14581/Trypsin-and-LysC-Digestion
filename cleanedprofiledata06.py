import pandas as pd 
import math

def get_Status(ksite, freq):
    if 'NoSite' in ksite:
        return 'NoSTY'
    elif 'NoSite' not in ksite and math.isnan(freq):
        return 'NDP'
    else:
    	return 'DP'

firstdf = pd.read_excel("UncatKProfMapDataLysC2.xlsx")
# seconddf = pd.read_excel("UncatRProfMapDataTrypsin2.xlsx")

kindf = pd.read_csv(r"C:\Users\jabir\Downloads\kinase_with_accession (1).csv")

print(kindf.columns)

# df = firstdf._append(seconddf)
df = firstdf

df["Enzyme"] = 'LysC'

df = df[['Gene_x', 'GeneSite','Peptides', 'pepcount' , 'exp_condition_count', 'Enzyme']]

df.rename(columns = {'Gene_x':'Kinase','GeneSite':'KinaseSite','pepcount':'PeptideCount','exp_condition_count':'Frequency'}, inplace = True) 

df = df.merge(kindf, how = "inner", left_on = "Kinase", right_on = "mapped_gene")

df.drop(columns = "mapped_gene", inplace = True)

df['Status'] = df.apply(lambda row: get_Status(row['KinaseSite'], row['Frequency']), axis=1)


df.to_excel("KHumanKinaseFastaLysC2.xlsx", index = False)