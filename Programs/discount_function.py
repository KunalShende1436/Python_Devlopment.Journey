def discount_price(original_price, discount_percentage):
    discount_price = original_price - (original_price * discount_percentage / 100)
    print(
        f"Discount price is {discount_price},after {discount_percentage}% on the original price {original_price}"
    )


discount_price(
    int(input("Enter Original price= ")), int(input("Enter Discount percentage % ="))
)
