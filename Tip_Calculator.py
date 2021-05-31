print("Hello, welcome to the tip calculator!")

bill_total = input("What is your bill total? ")
bill_total_float = float(bill_total)

people_number = input("How many people are splitting the bill? ")
people_number_int = int(people_number)

tip_amount = input("What percentage do you want the tip to be? No percentage signs ")
tip_amount_int = int(tip_amount)

tip_total = ((bill_total_float / people_number_int) * (1 + (tip_amount_int / 100)))
final_amount = (round(tip_total, 2))

print(f"Your total bill should be ${final_amount}")
