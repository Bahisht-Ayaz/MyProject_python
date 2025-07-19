import pandas as pa
import lxml
from openpyxl.workbook import Workbook

# rishta_profile = {
#     "Name" : ["Ali","Sana","Sania","Zohaib","Hassan"],
#     "Age" : [27,24,22,30,29],
#     "Gender" : ["M","F","F","M","M"],
#     "Prefered_caste" : ["Khan","Syed","Siddiqui","Sheikh","Qureshi"],
#     "Prefered_area" : ["Nazimabad","Defence","Clifton","Shah-e-faisal","Gulistan_e_Johar"],
#     "Profession" : ["Engineer","Doctor","Teacher","CA","Graphic Designer"],
#     "No_of_siblings" : [2,4,3,0,5]
# }
# df_rprofile = pa.DataFrame(rishta_profile)
#
# print(df_rprofile[df_rprofile["Prefered_caste"]=="Pathan"])
# print(df_rprofile[df_rprofile["No_of_siblings"]>2])
# print(df_rprofile[df_rprofile["Prefered_area"]=="Defence"])
# print(df_rprofile[(df_rprofile["Gender"]=="F") & (df_rprofile["Prefered_area"]=="Nazimabad")])
#
# # ADD COLUMN
# df_rprofile["Marital_status"]=["Single","Single","Divorce","Divorce","Single"]
# df_rprofile["Nationality"]="Pakistani"
# del df_rprofile["Profession"]
#
# print(df_rprofile)
dishes = {
    "Name" : ["Biryani","Zinger burger","Pizza","Alferado pasta","Malai boti","Broast"],
    "Price" : [250,560,2000,700,780,340],
    "Category" : ["Desi","Fast Food","Italian","Italian","BBQ","Fast Food"],
    "Main_ingredient" : ["Rice","Bun","Pita bread","Pasta","Chicken","Chicken"],
    "Quantity" : [10,25,30,9,55,0],
    "Status" : ["available","available","unavailable","unavailable","available","available"]
}
df_dishes = pa.DataFrame(dishes)
df_dishes["Country"]=["Pakistan","Trinidad & Tobago","Italy","Italy","Pakistan","Pakistan"]
df_dishes["Sale_price"]=[200,480,1500,600,650,320]
print(df_dishes[df_dishes["Price"]>500])
print(df_dishes[df_dishes["Status"]=="available"])
print(df_dishes[(df_dishes["Status"]=="available") & (df_dishes["Category"]=="Fast Food")])
print(df_dishes[df_dishes["Name"]=="Biryani"])
print(df_dishes[(df_dishes["Status"]=="available") & (df_dishes["Price"]>1500)])
choice = input("Enter c - CSV\nx - XML\nj - JSON\ne - EXCEL")
if(choice.lower() == "c"):
    df_dishes.to_csv("MYCSVFILE.csv",index=False)
elif(choice.lower() == "x"):
    df_dishes.to_xml("MYXMLFILE.xml")
elif(choice.lower() == "j"):
    df_dishes.to_json("MYJSONFILE.js")
elif(choice.lower() == "e"):
    df_dishes.to_excel("MYEXCELFILE.xlsx",index=False)
else:
    print("Invalid Input")
print(df_dishes)