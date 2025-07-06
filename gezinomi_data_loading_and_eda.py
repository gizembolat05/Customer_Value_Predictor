import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df=pd.read_excel("C:/Users/gizemb/Downloads/miuul_gezinomi.xlsx")
df. head()
df.info
df.describe().T
df.columns
df.isnull().values.any()
df.isnull().sum()
df.shape

df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()
df["ConceptName"].nunique()
df["ConceptName"].value_counts()
df.head()
df.groupby("SaleCityName").agg({"Price": "sum"})
df.groupby("ConceptName").agg({"Price": "sum"})
df.groupby("SaleCityName").agg({"Price":"mean"})
df.groupby("ConceptName").agg({"Price":"mean"})
df.groupby(["SaleCityName", "ConceptName"]).agg({"Price":"mean"}).reset_index()