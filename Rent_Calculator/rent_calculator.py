#input
rent=int(input("Enter your hostel flat rent: "))
food=int(input("Enter your food expenses: "))
electricity_spend=int(input("Enter your electricity bill: "))
charge_per_unit=int(input("Enter your charge per unit: "))
persons=int(input("Enter number of persons living in flat: "))
#output
total_bill=rent+food+(electricity_spend*charge_per_unit)
print("Total bill of flat is: ",total_bill)
output=total_bill/persons
print("Each person has to pay: ",output)    