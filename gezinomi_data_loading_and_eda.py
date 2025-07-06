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

bins=[-1,7,30,90,df["SaleCheckInDayDiff"].max()]
labels=["Minuters","Potential Planners","Planners","Early Bookers"]
df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins=bins, labels=labels)
df.head().reset_index()

df.groupby(["SaleCityName","ConceptName","EB_Score"]).agg({"Price":["mean","count"]}).reset_index()

df.groupby(["SaleCityName","ConceptName","Seasons"]).agg({"Price":["mean","count"]}).reset_index()

df.groupby(["SaleCityName","ConceptName","CInDay"]).agg({"Price":["mean","count"]}).reset_index()

agg_df=df.groupby(["SaleCityName","ConceptName","Seasons"]).agg({"Price":"mean"}).sort_values("Price",ascending=False)
agg_df.head(20)

agg_df.reset_index(inplace=True)
agg_df.head(20)

agg_df["sales_level_based"] = agg_df[["SaleCityName","ConceptName","Seasons"]].apply(lambda x: "_".join(x).upper(),axis=1)
agg_df.head(20)
df.head()

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"],4,labels=["D","C","B","L"])
agg_df.groupby("SEGMENT").agg({"Price":["mean","max","sum"]})

agg_df.sort_values(by="Price")

agg_df[agg_df["sales_level_based"]=="ANTALYA_HERŞEY DAHIL_HIGH"]
agg_df[agg_df["sales_level_based"]=="GIRNE_YARIM PANSIYON_LOW"]
agg_df[agg_df["sales_level_based"]=="İZMIR_HERŞEY DAHIL_LOW"]
agg_df[agg_df["sales_level_based"]=="MUĞLA_HERŞEY DAHIL_HIGH"]