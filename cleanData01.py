import pandas as pd 
import re 

def get_STY_positions(peptides, proseq):
    peptides = eval(peptides)
    all_STY_positions = {}
    for peptide in peptides:
    	peptide_positions = [m.start() for m in re.finditer(peptide, proseq)]
    	positions_S = [m.start() for m in re.finditer('S', proseq)]
    	positions_T = [m.start() for m in re.finditer('T', proseq)]
    	positions_Y = [m.start() for m in re.finditer('Y', proseq)]
    	matching_positions_S = [pos for pos in positions_S if any(start <= pos < start + len(peptide) for start in peptide_positions)]
    	matching_positions_T = [pos for pos in positions_T if any(start <= pos < start + len(peptide) for start in peptide_positions)]
    	matching_positions_Y = [pos for pos in positions_Y if any(start <= pos < start + len(peptide) for start in peptide_positions)]
    	peptide_positions = {}  
    	if matching_positions_S:
    		peptide_positions['S'] = [f"S{pos + 1}" for pos in matching_positions_S]
    	if matching_positions_T:
    		peptide_positions['T'] = [f"T{pos + 1}" for pos in matching_positions_T]
    	if matching_positions_Y:
    		peptide_positions['Y'] = [f"Y{pos + 1}" for pos in matching_positions_Y]
    	if peptide_positions:
    		all_STY_positions[peptide] = ', '.join([value for values in peptide_positions.values() for value in values])
    	else:
    		all_STY_positions[peptide] = 'NoSite'


    return all_STY_positions

def findposition(x):
    print("Im in Doo")
    result = []
    for key,value in x.items():
        temp = []# temp =[key,:,values]
        temp.append(key)
        temp.append(":")
        temp.append(value)
        protein_sequence = temp[0]
        positions = temp[2:]
        formatted_positions = ', '.join(positions)
        result_list = [f"{protein_sequence}: {formatted_positions}"]
        if not result_list:
            continue
        else:
            result.append(result_list)
    return result


def count05(x):
    filtered_list = []
    for dictionary in x:
        dictionary = str(dictionary[0])
        data = dictionary.split(":")[0]
        print(data)
        if len(data)<6:
            filtered_list.append(dictionary)
        else:
            continue
    return filtered_list


def count615(x):
    filtered_list = []
    for dictionary in x:
        dictionary = str(dictionary[0])
        data = dictionary.split(":")[0]
        print(data)
        if 5<len(data)<16:
            filtered_list.append(dictionary)
        else:
            continue
    return filtered_list


def count16a(x):
    filtered_list = []
    for dictionary in x:
        dictionary = str(dictionary[0])
        data = dictionary.split(":")[0]
        print(data)
        if len(data)>15:
            filtered_list.append(dictionary)
        else:
            continue
    return filtered_list

df = pd.read_excel("KLysC2.xlsx") 

print(df.columns)

fasta_df = df.groupby(['Gene', 'Accession'])['Fasta'].apply(''.join).reset_index()
fasta_df.rename(columns = {'Fasta':'completefasta'}, inplace = True) 
fasta_df = fasta_df.drop(['Accession'], axis=1)


print(fasta_df.columns)

df = df.merge(fasta_df, how = "inner", on = "Gene")
print(df.columns)

df['KSTY_positions'] = df.apply(lambda row: get_STY_positions(row['Kmiss_cleavage2'], row['completefasta']), axis=1)
# df['RSTY_positions'] = df.apply(lambda row: get_STY_positions(row['Rmiss_cleavage2 '], row['completefasta']), axis=1)

Ktotal = df["KSTY_positions"].count()
# Rtotal = df["RSTY_positions"].count()
 
df['KSTY_positions'] = df['KSTY_positions'].apply(findposition)
# df['RSTY_positions'] = df['RSTY_positions'].apply(findposition)

df['Kamino_acid_count_0to5'] = df['KSTY_positions'].apply(count05)
# df['Ramino_acid_count_0to5'] = df['RSTY_positions'].apply(count05)

df['Kamino_acid_count_6to15'] = df['KSTY_positions'].apply(count615)
# df['Ramino_acid_count_6to15'] = df['RSTY_positions'].apply(count615)

df['Kamino_acid_count_15to..'] = df['KSTY_positions'].apply(count16a)
# df['Ramino_acid_count_15to..'] = df['RSTY_positions'].apply(count16a)

df.to_excel("KLysC2.xlsx", index=False)  