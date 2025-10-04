import pandas as p 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#  training
data = p.read_csv("diabetes2.csv")

data = data.replace({"Yes":1 ,"No":0 ,"yes":1 ,"no":0})
x = data[["Glucose","BloodPressure","BMI","Insulin","DiabetesPedigreeFunction"]]
y = data["Outcome"]
data = data.dropna()

xtrain,xtest,ytrain,ytest =train_test_split(x,y,test_size = 0.3,random_state=50)

model = LogisticRegression(max_iter=1000)
model.fit(xtrain , ytrain)

BMI = float(input("Enter BMI : " ))
Glucose = float(input("Enter Glucose : "))
BloodPressure = float(input("Enter BloodPressure : "))
Insulin = float(input("Enter Insulin : "))
DiabetesPedigreeFunction = float(input("Enter DiabetesPedigreeFunction : "))

user_input = [[BMI , Glucose , BloodPressure , Insulin , DiabetesPedigreeFunction]]
prediction = model.predict_proba(user_input)
predict = prediction[0][0]
predictioninpercent = prediction[0][0]*100

if(predictioninpercent >= 50):
    print(f"aap ko sugar  kay itney {predictioninpercent:.2f}% chances hai")
else:
    print(f"aap ko sugar nhi hosakti you are save")