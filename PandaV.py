import pandas as pd

df = pd.read_csv(r"C:\Users\pedro.rrocha\Downloads\funcionarios.csv")


print(df.loc[0:8, 'nome':'lucro'])

print(df.iloc[0:8, 0:4])

salario = df.query("salario > 3000 and ativo == True")


