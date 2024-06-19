import pandas as pd

given_list = [1,2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 83, 84, 87, 88, 89, 91, 92, 94, 95, 97, 98, 99, 106, 110, 111, 112, 114, 116, 119, 120, 122, 128, 142, 143, 145, 159, 206, 211, 219, 295]
Kempty_dict = {key: [] for key in given_list + [-x for x in given_list]}
Rempty_dict = {key: [] for key in given_list + [-x for x in given_list]}

def categorize(x, flag):
    if flag ==0:
        for element in x:
            for items in element:
                print(items)
                part_0 = items.split(":")[0]
                print(part_0)
                part_1 = items.split(":")[1]
                count = len(part_0)
                print(count)
                if ('S' in part_0) or ('T' in part_0) or ('Y' in part_0):
                    part = part_0 + ':' + part_1
                    if count in Kempty_dict:
                        Kempty_dict[count].append(part)
                    else:
                        continue
                else:
                    count = -count
                    print(count)
                    if count in Kempty_dict:
                        Kempty_dict[count].append(part_0)
                    else:
                        continue
    elif flag == 1:
        for element in x:
            for items in element:
                part_0 = items.split(":")[0]
                part_1 = items.split(":")[1]
                count = len(part_0)
                if ('S' in part_0) or ('T' in part_0) or ('Y' in part_0):
                    part = part_0 + ':' + part_1
                    if count in Rempty_dict:
                        Rempty_dict[count].append(part)
                    else:
                        continue
                else:
                    count = -count
                    print(count)
                    if count in Rempty_dict:
                        Rempty_dict[count].append(part_0)
                    else:
                        continue


df = pd.read_excel('KLysC2.xlsx')



df['KSTY_positions'] = df['KSTY_positions'].apply(lambda x: eval(x))
# df['RSTY_positions'] = df['RSTY_positions'].apply(lambda x: eval(x))

df['KSTY_positions'].apply(categorize, flag =0)
# df['RSTY_positions'].apply(categorize, flag =1)



for key, value in Kempty_dict.items():
    Kempty_dict[key] = '; '.join(value)
# for key, value in Rempty_dict.items():
#     Rempty_dict[key] = '; '.join(value)


Kdf = pd.Series(Kempty_dict)
# Rdf = pd.Series(Rempty_dict)


Kdf = pd.DataFrame({'Category': Kdf.index, 'Peptides': Kdf.values})
# Rdf = pd.DataFrame({'Category': Rdf.index, 'Peptides': Rdf.values})


Kdf.to_excel("KCategorizedDataLysC2.xlsx", index = False)
# Rdf.to_excel("RCategorizedDataTrypsin2.xlsx", index = False)

