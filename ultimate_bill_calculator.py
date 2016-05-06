total_bill = int(raw_input("How much is the bill not including tip?"))
input = str(raw_input("Did you dine alone? Y or N"))
total_people = int(raw_input("How many people were at dinner?"))
eighteen = str(raw_input("Is 18% tip okay? Y or N"))
tip_percent = float(raw_input("How much do you want to leave for tip?"))

def tip_amount(total_bill, tip_percent):
	return total_bill * tip_percent

tip = tip_amount(total_bill, tip_percent)

def bill_with_tip(total_bill, tip_amount):
	return total_bill + tip

print bill_with_tip(total_bill, tip_amount)

final_bill = bill_with_tip(total_bill,tip_amount)

def per_person(final_bill, total_people):
	return final_bill/ total_people

print per_person(final_bill, total_people)

#amount_per_person = per_person()

#print original_bill_amount


#if input == "Y":

#else: 
#	int(raw_input("How many people were at dinner?")
