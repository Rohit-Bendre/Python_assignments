total_products=int(input("Enter number of products: "))
delvery_charge=0
discount=0
subtotal=0
products=[]
for i in range(total_products):
    id=i+1
    price=int(input(f"Enter price for your product {id}:"))
    quantity=int(input(f"Enter quantity for your product {id}:"))
    total_price=price*quantity
    subtotal+=total_price
    products.append([id,price,quantity,total_price])
    print("-"*50)

if subtotal>3000:
        discount+=(subtotal/100)*10
if subtotal<1500:
        delvery_charge+=100
grand_total=subtotal+delvery_charge-discount

print("Subtotal of all products: ",subtotal)
print("Total Discount: ",discount)
print("Total Delivery Charge: ",delvery_charge)
print("Final Amount to be paid: ",grand_total)