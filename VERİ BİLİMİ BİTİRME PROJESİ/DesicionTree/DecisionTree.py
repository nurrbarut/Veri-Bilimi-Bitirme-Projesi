import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Nur/Documents/dava_sonuclari.csv")

print("Eksik değerler:\n", df.isnull().sum())

Q1 = df["Case Duration (Days)"].quantile(0.25)
Q3 = df["Case Duration (Days)"].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df["Case Duration (Days)"] < (Q1 - 1.5 * IQR)) | 
          (df["Case Duration (Days)"] > (Q3 + 1.5 * IQR)))]

X = df.drop("Outcome", axis=1)
y = df["Outcome"]
X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
print("F1-Score:", f1_score(y_test, y_pred, zero_division=0))

plt.figure(figsize=(20,10))
plot_tree(model, feature_names=X.columns, class_names=["0","1"], filled=True, max_depth=3, fontsize=10)
plt.show()