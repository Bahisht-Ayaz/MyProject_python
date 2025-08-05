import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my_db"
)
db_info = con.cursor()
print("********* Student Info *********")
name = input("Enter student name : ")
guardian_name = input("Enter Guardian name : ")
phoneno = input("Enter Father phone number : ")
address = input("Enter your address : ")

query = "INSERT INTO `student`(`name`, `guardian_name`, `father_phone_no`, `address`) VALUES (%s,%s,%s,%s)"
value = (name,guardian_name,phoneno,address)
run = db_info.execute(query,value)
con.commit()

print(f"{name} Data has been saved successfully")
con.close()