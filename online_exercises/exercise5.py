wallet = float(input("Enter "
          "your wallet balance: $"))
item_price = float(input("Enter "
             "the price of the item: $"))

if wallet >= item_price:
    print("Purchase successful! ")
else:
    print("Insufficient funds ")
