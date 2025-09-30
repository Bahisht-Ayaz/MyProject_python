import pandas as p
import matplotlib .pyplot as map
from sklearn.linear_model import LinearRegression

mydata = p.read_excel("LRExample.xlsx")
X= mydata[["Hours Studied (X)"]]
Y= mydata[["Marks (Y)"]]

X = X.dropna()
Y = Y.loc[X.index]

model = LinearRegression()
model.fit(X,Y)

print(f"m value = {model.coef_[0]:.2f}")
print(f"b value = {model.intercept_[0]:.2f}")

hours_study = float(input("Enter Hours studied : "))
predict_value = model.predict([[hours_study]])

print(f"On {hours_study} Study hours\nMarks will be{predict_value[0]:.2f}")