import pandas as pd 

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 83, 84, 87, 88, 89, 91, 92, 94, 95, 97, 98, 99, 106, 110, 111, 112, 114, 116, 119, 120, 122, 128, 142, 143, 145, 159, 206, 211, 219, 295]

given_list += [-x for x in given_list]
print(given_list)

def rnan(x):
	if x == 'nan_nan':
		return None
	else:
		return x

def rnann(x):
	if x == 'nan':
		return None
	else:
		return x

def do(x):
    x = str(x)
    x = x.split(',')
    if len(x) == 1 and x[0] == 'nan':
        return 0
    else:
        return len(x)


maindf = pd.read_excel(r"KProfMapDataLysC2.xlsx")
# maindf = pd.read_excel(r"RProfMapDataTrypsin2.xlsx")
branchdf = pd.read_excel(r"C:\Users\jabir\Downloads\profile_frequency_without_isoforms_kinase.xlsx")
branchdf['GeneSite'] = branchdf['mapped_gene'].str.strip() + '_' + branchdf['mapped_phosphosite'].str.strip()
df = maindf.merge(branchdf, how='left', on='GeneSite')
df = df[['PepGeneSite', 'Peptides', 'pepcount', 'GeneSite', 'Gene_x', 'Sites', 'exp_condition_count']]
for num in given_list:
    # Check if the number is not in the column
    if num not in df['pepcount'].values:
        # Add the number to the column
        df = df._append({'pepcount': num}, ignore_index=True)
df = df.drop_duplicates()
df.to_excel("UncatKProfMapDataLysC2.xlsx", index=False)
# df.to_excel("UncatRProfMapDataTrypsin2.xlsx", index=False)


# newdf = df.copy()
# newdf['GeneSiteFreq'] = newdf['GeneSite'].astype(str) + "_" + newdf['exp_condition_count'].astype(str)

# # Grouping and aggregating by 'pepcount' and joining values of 'GeneSiteFreq' and 'Peptides'
# newdf['GeneSiteFreq'] = newdf['GeneSiteFreq'].astype(str)
# newdf['Peptides'] = newdf['Peptides'].astype(str)
# newdf = newdf.groupby('pepcount').agg({
#     'GeneSiteFreq': ', '.join,
#     'Peptides': ', '.join
# }).reset_index()
# print(newdf.head())
# newdf['frequency'] = newdf['Peptides'].apply(do)
# newdf['GeneSiteFreq'] = newdf['GeneSiteFreq'].apply(rnan)
# newdf['Peptides'] = newdf['Peptides'].apply(rnann)

# newdf1 = pd.DataFrame()

# newdf1['Neg Category'] = newdf['pepcount'].iloc[:110].copy()
# newdf1['Neg Peptides'] = newdf['Peptides'].iloc[:110].copy()
# newdf1['Neg frequency'] = newdf['frequency'].iloc[:110].copy()
# newdf1['Category'] = newdf['pepcount'].iloc[110:].copy().reset_index(drop=True)
# newdf1['Peptides'] = newdf['Peptides'].iloc[110:].copy().reset_index(drop=True)
# newdf1['frequency'] = newdf['frequency'].iloc[110:].copy().reset_index(drop=True)
# columns_to_sort = ['Neg Category', 'Neg Peptides', 'Neg frequency']

# # Sorting the selected columns based on 'Neg Category'
# sorted_columns = newdf1[columns_to_sort].sort_values(by='Neg Category', ascending=False)

# # Rearranging the selected columns based on the sorted order
# newdf1[columns_to_sort] = sorted_columns.values
# newdf1.to_excel("CatKGeneSitesCleave0.xlsx", index=False)
