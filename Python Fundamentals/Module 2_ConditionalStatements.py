"""
Conditional Expressions = when conditional statements are wrtitten in a single line they become condiional expressions
"""


def conExp():
    num = 60
    output = "This is the first preference of the output as the condition is true"
    return output if num < 50 else "The condion is false, this is the alternate output"


print(f"the result is :  {conExp()}")

"""
Price Discount
"""


def discount(price):
    if price >= 300:
        return "Congratulations! You are eligibale for 30% discount!! Here's your price -> ", +price-price*0.3
        # or  price *=0.7 (1-0.3)
    elif price >= 200:
        return "Congratulations! You are eligibale for 20% discount!! Here's your price -> ", +price-price*0.2
    elif price >= 100:
        return "Congratulations! You are eligibale for 10% discount!! Here's your price -> ", +price-price*0.1
    elif price in range(0, 100):   # this can also be written as - price<100 and price>=0
        return "Oopss! You are not eligibale for any discount. Here's your price -> ", +price
    else:
        return "Price out of discount range"


print(discount(50))
print(discount(150))
print(discount(250))
print(discount(350))
print(discount(450))
