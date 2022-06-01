id = input("Please, introduce your ID? ")
total_sales = float(input("How much do your sales amount to? "))
comm_percentage = 13

commission = round(total_sales * comm_percentage / 100,2)

print(f"{id} your commission this month ascend to {commission}$")
