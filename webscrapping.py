import pandas
import requests
from bs4 import BeautifulSoup

web_url = "https://www.pchotels.com/hotel-and-resort/pearl-continental-hotel-karachi?gad_source=1&gad_campaignid=22773155038&gbraid=0AAAAADMyAoh4BPCCqnNiRHO5vvdU-QYQt&gclid=Cj0KCQjw-ZHEBhCxARIsAGGN96KDYp3gVxjY2K--jDmC7139P79e4rUDoV-QAUe__Bxl5OVB0f7j_ZIaAs3qEALw_wcB"
response = requests.get(web_url)
print(response)
data_uthao = BeautifulSoup(response.text,"html.parser")
div_lao = data_uthao.find_all("div",class_="accomodation-content-bx")
h3=data_uthao.find_all("h3")
Roomname,Description=[],[]

for room in div_lao:
    h3_lao = room.find_all("h3")
    p_lao = room.find_all("p")
    for name in h3_lao:
     Roomname.append(name.text)
    for des in p_lao:
     Description.append(des.text)

Room_data = {
"Roomname":Roomname,
"Description":Description
}

room_df = pandas.DataFrame(Room_data)
print(room_df)
room_df.to_csv("Room_Data.csv",index=False)