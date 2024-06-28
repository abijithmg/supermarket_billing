import logging
logger = logging.getLogger(__name__)

# Simulation of Simple Super Market billing with group discount offers
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
        # logger.debug("Item Dict: %s", self.cart_items)
        for item, quantity in self.cart_items.items():
            # if item has discount price, then calculate the total price with discount
            if self.product[item]['discount_price']:
                total += self.calculate_discounted_price(quantity, self.product[item]['price'], self.product[item]['discount_quantity'], self.product[item]['discount_price'])
            else:
                total += quantity * self.product[item]['price']

        return total

    # If particular item is purchased in bulk or group(2 or more same items in the cart), then apply bulk discount price 
    def calculate_discounted_price(self, quantity, individual_price, group_size, group_price):
        group_count = quantity // group_size
        individual_count = quantity % group_size
        result = group_count * group_price + individual_count * individual_price
        # logger.debug(f"group_count:{group_count}, individual_count:{individual_count}, result:{result}")
        return result

# Main function to run the program
if __name__ == "__main__":
    checkout = Checkout()

    input_cart_items = input("Enter the items in the cart [Example: A, AB, CDBA, AAA, BAB etc]:\n")
    for item in input_cart_items:
        if item:
            checkout.scan(item)
            total_price = checkout.calculate_total()
        else:
            total_price = 0

    print(f"Total price: {total_price}")