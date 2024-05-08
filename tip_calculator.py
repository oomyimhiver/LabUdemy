#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
totolbill = input("What was the total bill? $")
persenoftip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ") 
totolbill_as_float = float(totolbill)
persenoftip_as_int = int(persenoftip)
people_as_int = int(people)
tip = totolbill_as_float*(persenoftip_as_int/100) +totolbill_as_float
tip_one_person = tip/people_as_int
tip_per_person = round(tip_one_person,2)
final_amount = "{:.2f}".format(tip_per_person)
print(f"Earch person should pay {final_amount}")
