import pandas as pd
import numpy as np
import lxml

# a = [1, 7, 2]
# # dataset = pd.Series(a)
# dataset = pd.Series(a, index=['x', 'y', 'z'])
# print(dataset)
# print(dataset['x'])

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index= ["day1", "day3"])
# print(myvar)

# s1 = pd.Series(['200', '100', 'python', '300.12', 'java', '400'])
# print(s1)
# s2 = pd.to_numeric(s1, errors='coerce')
# s2 = pd.Series(s2)
# print(s2.__sizeof__())
# new_s2 = pd.Series(s2).sort_values()
# print(new_s2)
# print(s2)

# sr1 = pd.Series([1, 2, 3, 4, 5])
# sr2 = pd.Series([2, 4, 6, 8, 10])

# result = sr1[~sr1.isin(sr2)]
# print(result)
# sr11 = pd.Series(np.union1d(sr1, sr2))
# print(sr11)
# sr22 = pd.Series(np.intersect1d(sr1, sr2))
# print(sr22)
# result = sr11[~sr11.isin(sr22)]
# print(result)

# lst = [[1, "John", 5.0], [2, 'Mary', 4.5], [3, 'Jack', 4.1]]
# df = pd.DataFrame(lst, columns=["#", "Name", "Score"], index=["First", "Second", "Third"])
# print(df["Score"].name)
# print(df["Score"].dtype)
# print(df)
# print(df.loc["First"])
# print(df.iloc[1])
# df = df.drop("First")
# print(df)
# print(df.iloc[0:1])

url = "https://www.globes.co.il/portal/instrument.aspx?instrumentId=356621&mode=trades"
tbl = pd.read_html(url, encoding='utf-8')
print(type(tbl))