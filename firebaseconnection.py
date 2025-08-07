import firebase_admin
from firebase_admin import credentials,firestore

creden = credentials.Certificate("C:\\Users\\asp\\Desktop\\MyProject_python\\studentinfo.json")
firebase_admin.initialize_app(creden)

db=firestore.client()

print("Connection with firebase - firestore")

name=input("Enter Name : ")
fname=input("Enter Father name : ")
phone=input("Enter Phone no : ")
address=input("Enter Address : ")
english_marks=float(input("Enter English Marks : "))
math_marks=float(input("Enter Math Marks : "))
urdu_marks=float(input("Enter Urdu Marks : "))
total=english_marks+math_marks+urdu_marks
print(f"Total marks : {total}")
percentage=(total/300)*100
print(f"Percentage : {percentage}")



fetch_student = db.collection("Student").document()
fetch_student.set({
    "Name":name,
    "Father_name":fname,
    "Phone":phone,
    "Address":address,
    "English_marks":english_marks,
    "Maths_marks":math_marks,
    "Urdu_marks":urdu_marks,
    "Total":total,
    "Percentage":percentage
})
print("Student data added sucessfully")

