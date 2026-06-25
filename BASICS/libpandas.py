import pandas as pd
a={"index":[1,2,3,4,5],"marks":[99,65,43,89,67],"name":["ram","pam","om","kim","tim"],"cgpa":[8,7,6,9.6,5]
   }
df=pd.DataFrame(a)
ser=pd.Series(a)
print(df)
print(ser)
cs=pd.read_csv("BASICS/practice.csv")
print(cs)
print(cs.head())
print(cs.tail())
print(cs.info())
#single column
print(df["name"])
print(type(df["name"]))
print(type(df["marks"]))
#2 col
print(df[["name","marks"]])
print(type(df[["name","marks"]]))
# row
print(df.loc[[4]])
print(type(df.loc[[4]]))
print(df.loc[4])
print(type(df.loc[4]))
print(df[df["marks"]>45] )
print(df[(df["marks"]>45) | (df["cgpa"]>6.6)] )
print(df[df["name"]=="om"])
print(df[(df["name"]!="pam") | (df["cgpa"]<6)])
print(df[(df["marks"]<70) & (df["cgpa"]>=7)])
print(df.iloc[2])
print(df.iloc[:,2])
