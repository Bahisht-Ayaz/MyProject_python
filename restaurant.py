# restaurant_name="Mijaaz"
# address="Tariq road"
# speciality="Fast food"
# phone_number=310909998
# city_name="Karachi"
# is_fivestar=True

# restaurant_name=input("Enter restaurant name : ")
# address=input("Enter address : ")
# speciality=input("Enter speciality : ")
# phone_number=int(input("Enter phone number : "))
# city_name=input("Enter city name : ")
# is_fivestar=bool(input("Is fivestar : "))
# print(f"Restaurant name is {restaurant_name} \nAddress is {address} \nSpeciality is {speciality} \nPhone no is {phone_number} \nCity name is {city_name} \nIs Fivestar {is_fivestar}")


print("Dholu bholu halwa puri shop")
puries=int(input("How many puries do you want ?"))
choley=int(input("how many choley ki plates do you want ?"))
aalu=int(input("how many aalu ki plates do you want ?"))
halwa=int(input("how many halwey ki plates do you want ?"))
per_puri=50
per_choley_plate=100
per_aalu_plate=80
per_halwa_plate=150

puri_total=per_puri * puries
choley_total=per_choley_plate * choley
aalu_total=per_aalu_plate * aalu
halwa_total=per_halwa_plate * halwa

total_bill=puri_total + choley_total + aalu_total + halwa_total
tax=total_bill*0.16
total=total_bill+tax
discount=total*0.5
bill_after_discount=total - discount
print(f"Total bill is : {total_bill} \nTax is : {tax} \nTotal bill with tax is {total} \nDiscount is {discount} \nBill after discount is : {bill_after_discount}")