import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("food_calories.csv")

X = df[['Protein','Fat','Carbs']]
y = df['Calories']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(x_train, y_train)

pickle.dump(model, open('model.pkl','wb'))
print("Model Saved as model.pkl")
