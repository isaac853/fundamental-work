

def discountprice(price: float ,discount: float) -> float:
    """takes a price as a float and applies a percent discount amount and returns discounted price"""
    price = price * (1- (discount / 100))
   
   #attempt at rounding to 2d.p, failed as i can't cast augmented variables 

   # price = str(price)

    # for i in range(len(price)):
    #     temp = price[i+3]
    #     temp1 = price[i+3]
    #     temp2 = price[i+2]
    #     if price[i] == "." and int(temp) >= 5:
            
    #         float(temp2) += 1
    #         price = float(price) - (float(temp1) * (10 ** (-1*(len(str(temp1))+2))))

    #     elif price[i] == ".":
    #         price = float(price) - (float(temp1) * (10 ** (-1*(len(str(temp1))+2))))


    return float(price)



price = input("enter a price ")
discount = input("enter a discount ")
print(discountprice(price, discount))