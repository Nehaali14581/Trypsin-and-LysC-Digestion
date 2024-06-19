import pandas as pd 

def do(x):
	# print(x)
	gene = x[0]
	peptides = x[1]
	peptides = eval(peptides)
	nlist = []
	for elements in peptides: #[['MK: S1,S2,S3']]
		pepSites = elements[0].split(":")  #['MK','S1,S2,S3']
		peptide = pepSites[0] #'MK'
		if ('S' in peptide) or ('T' in peptide) or ('Y' in peptide):
			count = len(peptide) #2
		else:
			count = len(peptide)
			count = -count
		sites = pepSites[1].split(',') #['S1','S2','S3']
		sites = [(peptide + "_" + str(count) + ":" + gene + "_" + site.strip()) for site in sites] #['MK_2:Gene_S1']
		# print('Small',len(sites))
		for site in sites:
			nlist.append(site)
	# print('I am final',len(nlist))
	return nlist
	

df = pd.read_excel(r"KLysC2.xlsx")
new_df = pd.DataFrame()

df['GeneSites'] = df["Gene"].apply(lambda x: x.strip()) + "_" + df['KSTY_positions'].apply(lambda x: x.strip())
# df['GeneSites'] = df["Gene"].apply(lambda x: x.strip()) + "_" + df['RSTY_positions'].apply(lambda x: x.strip())
df['GeneSites'] = df['GeneSites'].apply(lambda x: x.split('_'))
new_df['PepGeneSite'] = df['GeneSites'].apply(do)
new_df = new_df.explode('PepGeneSite') 
print(new_df['PepGeneSite'])
new_df['PepGeneSite'].apply(lambda x: print(type(x)))
new_df["Peptides"] = new_df["PepGeneSite"].apply(lambda x: (str(x).split(":")[0]).split("_")[0]) #MK_2:AAK1_NoSite = [MK_2,AAK1_NoSite] = MK_2 = MK

new_df["pepcount"] = new_df["PepGeneSite"].apply(lambda x: (str(x).split(":")[0]).split("_")[-1]) #MK_2:AAK1_NoSite
new_df["GeneSite"] = new_df["PepGeneSite"].apply(lambda x: str(x).split(":")[-1])
new_df["Gene"] = new_df["GeneSite"].apply(lambda x: x.split("_")[0])
new_df["Sites"] = new_df["GeneSite"].apply(lambda x: x.split("_")[-1])
new_df.drop_duplicates(inplace = True)
new_df.to_excel("KProfMapDataLysC2.xlsx", index = False)
# new_df.to_excel("RProfMapDataTrypsin2.xlsx", index = False)

