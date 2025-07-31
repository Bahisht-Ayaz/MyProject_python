import os.path
import pandas
from pydriller import Repository

url = input("Enter repository link : ")
commitername,committeremail,date,projectname,commitmsg=[],[],[],[],[]
print(f"Fetching {url}")
for a in Repository(url).traverse_commits():
    commitername.append(a.author.name)
    committeremail.append(a.author.email)
    date.append(a.author_date)
    projectname.append(a.project_name)
    commitmsg.append(a.msg)
print("Fetching completed")
github_dic ={
    "Project Name" : projectname,
    "Name" : commitername,
    "Email":committeremail,
    "Message":commitmsg,
    "Date":date
}
github_df = pandas.DataFrame(github_dic)
file_name=input("Enter filename : ")
if os.path.exists(f"{file_name}.csv"):
    print(f"{file_name}already exist, please choose different name")
else:
    github_df.to_csv(f"{file_name}.csv",index=False)
    print("File created successfully")