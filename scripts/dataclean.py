import pandas as pp


df=pp.read_csv("data/mental_health_and_technology_usage_2024.csv")


print("\nOverviwe")
print(f"total rows: {len(df)}")
print(f"number of columns and lsit of all the columns: {len(df.columns), list(df.columns)}")
print("\nData types:")
print(df.dtypes)


print("\nMissing values check\n")

missing_val = df.isnull().sum()
if missing_val.sum()== 0:
    print("no missing values found")
else:
    print("name of the column and the number of values missing:")
    print(missing_val[missing_val>0])


print("\nData formatting checks per column")
issue=False
for column in df.columns:
        if df[column].apply(type).nunique()>1:
            print(f"Mixed data types in column '{column}'")
            issue = True
            
if not issue:
        print("no issues with formattign")


print(df.describe)



