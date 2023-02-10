import datetime as d
import random

date= d.date.today().strftime("%d/%m/%y")
time = d.datetime.now().strftime("%H:%M:%S")

db = {
    "blue pen": {"prod_id": 20063, "price": 20},
    "printer ": {"prod_id": 20064, "price": 6200},
    "monitor ": {"prod_id": 20065, "price": 8000},
    "laptop  ": {"prod_id": 20066, "price": 45000},
    "earphone": {"prod_id": 20067, "price": 2550},
    "guitar  ": {"prod_id": 20068, "price": 7000},
    "phone   ": {"prod_id": 20070, "price": 1550}
}

p = ""
q = ""
n = 1

cart = {}
bill_amount = 0

while True:
    try:
        p = str(input("Enter Product Name (Press Enter If Done!): ")).strip().lower()
        if p == "":
            break
        else:
            if len(p)!= 8:
                add_n = 8-len(p)
                p+= " "*add_n
            q = int(input("Enter Quantity: "))
            if q == "": q = "1"
            prod_list = {"prod_name": p, "quantity": int(q)}
            cart[f"Item{n}"] = prod_list
            # Price Calculations
            price = db[p]["price"]
            bill_amount += price*int(q)
            n += 1
    except (ValueError): print("Quantity should be in numbers!")
    except (KeyError): print("Item out of stock!")
    finally: pass

cart_count = len(cart)
bill_no = int(random.random()*100000)
gst = 6
gst_tax = (bill_amount*gst)/100

print(u"\t\t\t\t\t\t\t\t\tBILL\n")
print(f"\t\t\t\tBill Number \t\t\t\t\t\t\t{bill_no}\n\t\t\t\tCashier \t\t\t\t\t\t\tA Saha\n\t\t\t\tTime \t\t\t\t\t\t\t\t{time}\n\t\t\t\tDate \t\t\t\t\t\t\t\t{date}\n")
print("="*130,"\n")
print("\tPRODUCT ID\t\t\tPRODUCT NAME\t\t\tQUANTITY\t\t\t\tPRICE")
for i in range(1, cart_count+1):
    print(f'\t {db[cart[f"Item{i}"]["prod_name"]]["prod_id"]}', end="\t\t\t")
    print(f'\t {cart[f"Item{i}"]["prod_name"].upper()}', end="\t\t")
    print(f'\t {cart[f"Item{i}"]["quantity"]}', end="\t\t\t\t")
    print(f'\t {db[cart[f"Item{i}"]["prod_name"]]["price"]}')
print("-"*78,"\n")
print(f"\t\t\t\tSub Total \t\t\t\t\t\tRs. {bill_amount}")
print(f"\t\t\t\tGST/Taxes \t\t\t\t\t\tRs. {gst_tax}")
print(f"\t\t\t\tTOTAL     \t\t\t\t\t\tRs. {bill_amount+gst_tax}\n")
print("."*130,"\n")
