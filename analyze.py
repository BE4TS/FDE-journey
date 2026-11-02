import pandas as pd 
df=pd.read_csv("weather.csv")
print(df.describe())
df["Temperature_Range"]=df["max_temp_c"]-df["min_temp_c"]
print("maximum temperature range:",df.loc[df["Temperature_Range"].idxmax(),"date"])
print("Average minimum Temperature:", round(df["min_temp_c"].mean(),1))
print("Rainiest day: ",df.loc[df["rain_mm"].idxmax(),"date"],"(",df["rain_mm"].max(),")")
print("Hottest day: ",df.loc[df["max_temp_c"].idxmax(),"date"],"(",df["max_temp_c"].max(),")")