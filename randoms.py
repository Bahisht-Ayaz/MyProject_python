import randoms as rd

cities = ["Karachi", "Lahore", "Islamabad", "Faisalabad", "Hyderabad", "Multan", "Sheikhupura", "Sialkot", "Bahawalpur", "Sargodha"]

print(rd.sample(cities,3))
rd.shuffle(cities)
print(cities)
print(rd.choice(cities))