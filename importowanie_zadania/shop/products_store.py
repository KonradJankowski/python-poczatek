products = {
    "chleb" : {
        "quantity" : 100,
        "price" : 3.5
    },
    "jabka" : {
        "quantity" : 50,
        "price" : 3.2
    }
}

def update_product_quanity(product_name, ordered_quanity):
    products[product_name]["quantity"] -= ordered_quanity
