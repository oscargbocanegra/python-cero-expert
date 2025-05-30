def calculate_total(products):
    total = 0
    for product in products:
        total += product['price']
    return total

def test_calculate_total_with_empty_list():
    print("Testing with an empty list of products")
    assert calculate_total([]) == 0

def test_calculate_total_with_single_list():
    products = [{'name': 'Product 1', 'price': 100}]
    print("Testing with a single product")
    assert calculate_total(products) == 100

def test_calculate_total_with_multiple_products():
    print("Testing with multiple products")
    products = [
        {'name': 'Product 1', 'price': 100},
        {'name': 'Product 2', 'price': 200},
        {'name': 'Product 3', 'price': 300}
    ]
    assert calculate_total(products) == 600


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_list()
    test_calculate_total_with_multiple_products()
    print("All tests passed!")
    