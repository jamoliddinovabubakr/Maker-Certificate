import pandas as pd


def read_data_excell(file):
    data = pd.read_excel("." + file, header=None)
    df = pd.DataFrame(data)
    n = df.shape[0]
    users = []
    for i in range(n):
        user = []
        fam = df.iloc[i, 0]
        ism = df.iloc[i, 1]
        sharf = df.iloc[i, 2]
        jshshr = df.iloc[i, 3]
        invoice = df.iloc[i, 4]

        user.append(fam)
        user.append(ism)
        user.append(sharf)
        user.append(jshshr)
        user.append(invoice)

        users.append(user)

    return users
