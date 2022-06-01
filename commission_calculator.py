id = input("Whats your ID? ")
total_sales = float(input("How much do your sales amount to? "))

commission = round((total_sales*13)/100,2)

print(f"{id} your commission this month ascend to {commission}€")
