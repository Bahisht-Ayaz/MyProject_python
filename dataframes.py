import pandas as pa
rishta_profile = {
    "Name" : ["Ali","Sana","Sania","Zohaib","Hassan"],
    "Age" : [27,24,22,30,29],
    "Gender" : ["M","F","F","M","M"],
    "Prefered_caste" : ["Khan","Syed","Siddiqui","Sheikh","Qureshi"],
    "Prefered_area" : ["Nazimabad","Defence","Clifton","Shah-e-faisal","Gulistan_e_Johar"],
    "Profession" : ["Engineer","Doctor","Teacher","CA","Graphic Designer"],
    "No_of_siblings" : [2,4,3,0,5]
}
df_rprofile = pa.DataFrame(rishta_profile)

print(df_rprofile[df_rprofile["Prefered_caste"]=="Pathan"])
print(df_rprofile[df_rprofile["No_of_siblings"]>2])
print(df_rprofile[df_rprofile["Prefered_area"]=="Defence"])
print(df_rprofile[(df_rprofile["Gender"]=="F") & (df_rprofile["Prefered_area"]=="Nazimabad")])

# ADD COLUMN
df_rprofile["Marital_status"]=["Single","Single","Divorce","Divorce","Single"]
df_rprofile["Nationality"]="Pakistani"
del df_rprofile["Profession"]

print(df_rprofile)