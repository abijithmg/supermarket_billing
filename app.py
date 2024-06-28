# Guidelines:
# 1. Use Python3 to solve the problem.
# 2. Apply OOPs principles
# 3. Add Readme on how to run/setup
# 4. Added Bonus - Tests and dockerisation.

class Checkout:
    def __init__(self):
        self.cart_items = {}
        # this can be moved to DB table or external file for large number of products
        self.product = {
            'A':{
                'price': 50,
                'discount_price': 130,
                'discount_quantity': 3
            },'B':{
                'price': 30,
                'discount_price': 45,
                'discount_quantity': 2
            },'C': {
                'price': 20,
                'discount_price': None,
                'discount_quantity': None
            },'D': {
                'price': 15,
                'discount_price': None,
                'discount_quantity': None
            }
        }

    def scan(self, item):
        if item in self.cart_items:
            self.cart_items[item] += 1
        else:
            self.cart_items[item] = 1
    
    def calculate_total(self):
        total = 0
        self.cart_items = dict(sorted(self.cart_items.items()))
        # Can be changed to logger.debug during deployment
        print("[DEBUG] Item Dict: ", self.cart_items)
        for item, quantity in self.cart_items.items():
            if self.product[item]['discount_price']:
                total += self.calculate_discounted_price(quantity, self.product[item]['price'], self.product[item]['discount_quantity'], self.product[item]['discount_price'])
            else:
                total += quantity * self.product[item]['price']

        return total

    # If particular item is purchased in bulk or group(2 or more same items in the cart), then apply bulk discount price 
    def calculate_discounted_price(self, quantity, individual_price, group_size, group_price):
        group_count = quantity // group_size
        individual_count = quantity % group_size
        print(f"[DEBUG] group_count:{group_count}, individual_count:{individual_count}")
        return group_count * group_price + individual_count * individual_price

# Main function to run the program
checkout = Checkout()
input_cart_items = input("Enter the items in the cart [Example: A, AB, CDBA, AAA, BAB etc]:\n")
for item in input_cart_items:
    if item:
        checkout.scan(item)
        total_price = checkout.calculate_total()
    else:
        total_price = 0

print(f"Total price: {total_price}")