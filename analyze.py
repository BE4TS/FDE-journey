import pandas as pd 
df=pd.read_csv("weather.csv")
print(df.describe())
print("Rainiest day: ",df.loc[df["rain_mm"].idxmax(),"date"],"(",df["rain_mm"].max(),")")
print("Hottest day: ",df.loc[df["max_temp_c"].idxmax(),"date"],"(",df["max_temp_c"].max(),")")