import pandas as pd

df = pd.read_csv("C:/Users/Nur/Documents/country.csv")
df_sorted_population = df.sort_values(by="Population", ascending=False)
print(df_sorted_population[["Country", "Population"]])

df_sorted_gdp = df.sort_values(by="GDP ($ per capita)", ascending=True)
print(df_sorted_gdp[["Country", "GDP ($ per capita)"]])

df_population_above_10m = df[df["Population"] > 10000000]
print(df_population_above_10m[["Country", "Population"]])

df_literacy_top5 = df.sort_values(by="Literacy (%)", ascending=False).head(5)
print(df_literacy_top5[["Country", "Literacy (%)"]])

df_gdp_above_10000 = df[df["GDP ($ per capita)"] > 10000]
print(df_gdp_above_10000[["Country", "GDP ($ per capita)"]])

df_density_top10 = df.sort_values(by="Pop. Density (per sq. mi.)", ascending=False).head(10)
print(df_density_top10[["Country", "Pop. Density (per sq. mi.)"]])