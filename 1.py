import pandas
import re

df = pandas.read_csv("train.csv")

female = {}

for i in range(len(df)):
    if list(df['Sex'])[i] == 'female':
        name = list(df['Name'])[i].split(',')[1]
        name = re.findall(r'\.\s[\w]+|\([\w]+', name)

        name = name[len(name)-1]
        name = re.findall(r'[\w]+', name)
        if name[0] in female:
            female[name[0]] += 1
        else:
            female[name[0]] = 1

count = 0
for name in female.keys():
    if female[name] > count:
        count = female[name]
        frequent_name = name

print(f'The most popular name is {frequent_name} - {count}', sep='')
