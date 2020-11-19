import pandas

df = pandas.read_csv("train.csv")
female = {}

# -Female---------------------------------------------------------------------
Sex_female = df.query("Sex == 'female'")
adresses = ['miss', 'mrs', 'lady', 'the countess', 'mme', 'mlle']


for item in Sex_female['Name']:

    item = item.replace('.', ',').split(',')  # [0]  # .split(" ")[0]
    name = item[2].split(" ")[1]
    a = list(name)
    if '(' in a:

        del a[0]

        if (')' in a) or ('"' in a):

            ln = len(a) - 1
            del a[ln]

        name = "".join(a)

    adress = item[1].lower().strip()

    if adress in adresses:
        try:
            female[name] += 1
            print(name, female[name])
        except KeyError:
            female[name] = 1

# print(female)

# ---male-----------------------------------------------------------


# ----------------------------------------------------------------

print("Most common female name is '", frequent_name, "' ", count, sep="")
