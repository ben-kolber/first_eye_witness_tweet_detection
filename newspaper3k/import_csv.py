import pandas as pd
import re


# input file
data = pd.read_csv('/Users/benjaminkolber/Desktop/politics.csv', encoding="ISO-8859-1")

#data['A'] = '@' + data['A'].astype(str)

df = pd.DataFrame()
#df = data.loc[:, :'A']
tmp = list(data['A'])
#df = data.loc[data['B'] == 'right']
#df = df.append(data.loc[data['B'] == 'left'])
#df = df.append(data.loc[data['B'] == 'center'])

# Case 1 for cleaning (most common case)
list = []
for item in tmp:
    item = str(item)
    if "FollowFollow" in item:
        item = item.replace("FollowFollowÿ", "")
        item = item.replace("FollowFollowæ", "")
        item = item.replace("ÊÊÊÊÊÊÊÊÊÊÊÊÊÊÊÊ", "")
        item = item.replace("ÊÊÊÊ", "")
        item = item.replace("Ê", "")
        list.append(item)

# Case 2 for cleaning
for i in range(len(list)):
    pass
    #item = str("".join(item.split()))
    #item = ''.join(i for i in item if not i.isdigit())
    #list[i] = list[i].replace("æ FollowFollowæ", "")
    #list[i] = str("".join(list[i].split()))
    #list[i] = list[i].replace(".æ", "")
    #list[i] = list[i].replace("æææ", "")
    #list[i] = list[i].replace(".æ æ", "")
    #list[i] = list[i].replace("ææ", "")
    #list[i] = ''.join(i for i in list[i] if not i.isdigit())
    #list[i] = list[i].replace(".", "")

for item in list:
    print(item)

# output file
# list.to_csv('/Users/benjaminkolber/Desktop/panda_output.csv')
