import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("food_calories.csv")

print(df.head())
print(df.describe())

plt.bar(df['Food Item'], df['Calories'])
plt.xticks(rotation=45)
plt.title("Calories by Food Item")
plt.show()

sns.heatmap(df.corr(), annot=True)
plt.show()
