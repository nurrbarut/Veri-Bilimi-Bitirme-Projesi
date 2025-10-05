import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Nur/Documents/50_Startups.csv")

print(df.head())

print(df.columns)

sns.scatterplot(x="R&D Spend", y="Profit", data=df, color="purple", s=100)
plt.title("R&D Harcaması ve Kâr İlişkisi", fontsize=16, color="darkblue", fontweight="bold")
plt.style.use('ggplot')
plt.grid(True, linestyle="--", color="grey", alpha=0.6)
plt.xlabel("R&D Harcaması", fontsize=13, color="green", fontweight="bold")
plt.ylabel("Kâr", fontsize=13, color="green", fontweight="bold")
plt.show()

sns.scatterplot(
    x="Administration", 
    y="Profit", 
    data=df, 
    color="orange", 
    s=100
)
plt.title("Yönetim Harcaması ve Kâr İlişkisi", fontsize=16, color="darkred")
plt.style.use('ggplot')
plt.grid(True, linestyle="--", color="grey", alpha=0.6)
plt.xlabel("Yönetim Harcaması", fontsize=12, color="green")
plt.ylabel("Kâr", fontsize=12, color="green")
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ortalama_kar = df.groupby("State")["Profit"].mean().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(
    x="State", 
    y="Profit", 
    hue="State",     
    data=ortalama_kar,
    palette="Set2",
    legend=False
)

plt.title("Eyaletlere Göre Ortalama Kâr", fontsize=18, color="darkblue", fontweight="bold")
plt.xlabel("Eyalet", fontsize=14, color="black")
plt.ylabel("Ortalama Kâr", fontsize=14, color="black")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()

df_melt = df.melt(id_vars="State", 
                  value_vars=["R&D Spend", "Administration", "Marketing Spend"],
                  var_name="Harcamalar",
                  value_name="Değer")

plt.figure(figsize=(10, 6))
sns.boxplot(x="Harcamalar", y="Değer", hue="Harcamalar", data=df_melt, palette="Set3", dodge=False)

plt.title("R&D, Yönetim ve Pazarlama Harcamalarının Dağılımı", fontsize=18, color="darkred", fontweight="bold")
plt.xlabel("Harcama Türü", fontsize=14)
plt.ylabel("Harcanan Miktar", fontsize=14)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()