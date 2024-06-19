import pandas as pd
import re


def cleanK(x):
    Klist = []
    for i in x:
        if i.count('K')==3:
            Klist.append(i)
        else:
            continue
    print(Klist)
    return Klist

def cleanR(x):
    Rlist = []
    for i in x:
        if i.count('R')==2:
            Rlist.append(i)
        else:
            continue
    print(Rlist)
    return Rlist

def Lysc(sequence, missed_clevage=2, pep_min_len=1, pep_max_len=1000):
    print(sequence)
    get_dup_k = [i for i in range(len(sequence)) if sequence.startswith('K', i)]
    for i in get_dup_k:
        print(i)
    merge_list_fltrd_k = get_dup_k
    merge_list_fltrd_k.append(len(sequence))
    print(merge_list_fltrd_k)
    initialize_k = 0
    peptides_ending_k = []
    for iter_lst_k in range(len(merge_list_fltrd_k) - int(missed_clevage)):
        peptide_k = sequence[initialize_k: int(merge_list_fltrd_k[iter_lst_k + missed_clevage]) + 1]
        if peptide_k.endswith('K') and len(peptide_k) >= int(pep_min_len) and len(peptide_k) <= int(pep_max_len):
            peptides_ending_k.append(peptide_k) 
        initialize_k = merge_list_fltrd_k[iter_lst_k] + 1
        if not (peptide_k.endswith('K')) and len(peptide_k) >= int(pep_min_len) and len(peptide_k) <= int(pep_max_len):
            peptides_ending_k.append(peptide_k)
        initialize_k = merge_list_fltrd_k[iter_lst_k] + 1
    print(peptides_ending_k)

    return peptides_ending_k


def TRYPSIN(proseq, miss_cleavage=1):
    print("Im in Trypsin") 
    peptides_k = []
    peptides_r = []
    cut_sites = [0]
    for i in range(0, len(proseq) - 1):
        if proseq[i] == 'K' and proseq[i + 1] != 'P':
            cut_sites.append(i + 1)
        elif proseq[i] == 'R' and proseq[i + 1] != 'P':
            cut_sites.append(i + 1)

    if cut_sites[-1] != len(proseq):
        cut_sites.append(len(proseq))

    if len(cut_sites) > 2:
        if miss_cleavage == 0:
            for j in range(0, len(cut_sites) - 1):
                peptide = proseq[cut_sites[j]:cut_sites[j + 1]]
                if peptide.endswith('K'):
                    peptides_k.append(peptide)
                elif peptide.endswith('R'):
                    peptides_r.append(peptide)
                elif not (peptide.endswith('R') or peptide.endswith('K')):
                    peptides_k.append(peptide)
   
        elif miss_cleavage == 1:
            for j in range(0, len(cut_sites) - 2):
                peptide1 = proseq[cut_sites[j]:cut_sites[j + 1]]
                peptide2 = proseq[cut_sites[j]:cut_sites[j + 2]]
                if peptide1.endswith('K'):
                    peptides_k.append(peptide1)
                elif peptide1.endswith('R'):
                    peptides_r.append(peptide1)
                # elif not (peptide1.endswith('R') or peptide1.endswith('K')):
                    # peptides_k.append(peptide1)
 
                if peptide2.endswith('K'):
                    peptides_k.append(peptide2)
                elif peptide2.endswith('R'):
                    peptides_r.append(peptide2)
                # elif not (peptide2.endswith('R') or peptide2.endswith('K')):
                    # peptides_k.append(peptide2)

            last_peptide = proseq[cut_sites[-2]:cut_sites[-1]]
            if last_peptide.endswith('K'):
                peptides_k.append(last_peptide)
            elif last_peptide.endswith('R'):
                peptides_r.append(last_peptide)
            # elif not (last_peptide.endswith('R') or last_peptide.endswith('K')):
                    # peptides_k.append(last_peptide)

        elif miss_cleavage == 2:
            for j in range(0, len(cut_sites) - 3):
                peptide1 = proseq[cut_sites[j]:cut_sites[j + 1]]
                peptide2 = proseq[cut_sites[j]:cut_sites[j + 2]]
                peptide3 = proseq[cut_sites[j]:cut_sites[j + 3]]

                if peptide1.endswith('K'):
                    peptides_k.append(peptide1)
                elif peptide1.endswith('R'):
                    peptides_r.append(peptide1)
                # elif not (peptide1.endswith('R') or peptide1.endswith('K')):
                    # peptides_k.append(peptide1)

                if peptide2.endswith('K'):
                    peptides_k.append(peptide2)
                elif peptide2.endswith('R'):
                    peptides_r.append(peptide2)
                # elif not (peptide2.endswith('R') or peptide2.endswith('K')):
                    # peptides_k.append(peptide2)

                if peptide3.endswith('K'):
                    peptides_k.append(peptide3)
                elif peptide3.endswith('R'):
                    peptides_r.append(peptide3)
                # elif not (peptide3.endswith('R') or peptide3.endswith('K')):
                    # peptides_k.append(peptide3)

            before_last_peptide = proseq[cut_sites[-3]:cut_sites[-2]]
            last_peptide = proseq[cut_sites[-3]:cut_sites[-1]]

            if before_last_peptide.endswith('K'):
                peptides_k.append(before_last_peptide)
            elif before_last_peptide.endswith('R'):
                peptides_r.append(before_last_peptide)
            elif not (before_last_peptide.endswith('R') or before_last_peptide.endswith('K')):
                    peptides_k.append(before_last_peptide)

            if last_peptide.endswith('K'):
                peptides_k.append(last_peptide)
            elif last_peptide.endswith('R'):
                peptides_r.append(last_peptide)
            elif not (last_peptide.endswith('R') or last_peptide.endswith('K')):
                    peptides_k.append(last_peptide)

    else:  # there is no trypsin site in the protein sequence
        peptide = proseq
        print(peptide)
        if peptide.endswith('K'):
            peptides_k.append(peptide)
        elif peptide.endswith('R'):
            peptides_r.append(peptide)
        elif not (peptide.endswith('R') or peptide.endswith('K')):
                    peptides_k.append(peptide)

    return peptides_k, peptides_r


def count_amino_acids(peptides):
    print("Im in count amino")
    amino_acid_counts = {}
    for peptide in peptides:
         amino_acid_counts[peptide] = len(peptide)
    return amino_acid_counts


df = pd.read_excel(r"C:\CIODS\Updated_Trypsin_LysC\Updated_KinaseWith_Fasta.xlsx")


# df[['Kmiss_cleavage1', 'Rmiss_cleavage1']] = df['Fasta'].apply(lambda x: pd.Series(TRYPSIN(x)))
df['Kmiss_cleavage2'] = df['Fasta'].apply(Lysc)
df['Kmiss_cleavage2'] = df['Kmiss_cleavage2'].apply(cleanK)
# df['Rmiss_cleavage1'] = df['Rmiss_cleavage1'].apply(cleanR)
df['Kcount'] = df['Kmiss_cleavage2'].apply(lambda x: len(x))
# df['Rcount'] = df['Rmiss_cleavage1'].apply(lambda x: len(x))

df['Kamino_acid_count'] = df['Kmiss_cleavage2'].apply(count_amino_acids)
# df['Ramino_acid_count'] = df['Rmiss_cleavage1'].apply(count_amino_acids)

df.to_excel("KLysC2.xlsx", index=False)



